import argparse
from datetime import datetime, timedelta
import pytz

from dotenv import load_dotenv
load_dotenv()

from config import (
    DRAMAS, YOUTUBE_API_KEY, DATABASE_URL,
    SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, REPORT_TO, TZ
)
from db import get_engine, upsert_metric
from youtube_client import yt_build, find_video_for_date, get_video_stats
from mailer import send_report

def lk_today_date():
    tz = pytz.timezone(TZ)
    return datetime.now(tz).date()

def run_for_date(target_date):
    if not YOUTUBE_API_KEY:
        raise RuntimeError("Missing YOUTUBE_API_KEY")
    if not DATABASE_URL:
        raise RuntimeError("Missing DATABASE_URL")

    engine = get_engine(DATABASE_URL)
    youtube = yt_build(YOUTUBE_API_KEY)

    lines = []
    ok = 0
    not_found = 0
    errors = 0

    for d in DRAMAS:
        base_row = {
            "drama_key": d["drama_key"],
            "drama_name": d["drama_name"],
            "channel_key": d["channel_key"],
            "channel_name": d["channel_name"],
            "channel_id": d["channel_id"],
            "target_date": str(target_date),

            "video_id": None,
            "video_title": None,
            "video_url": None,
            "video_published_at": None,
            "views": None,
            "likes": None,
            "comments": None,
            "scrape_status": "NOT_FOUND",
            "scrape_note": None,
            "episode_number": None,
        }

        try:
            found = find_video_for_date(
                youtube=youtube,
                channel_id=d["channel_id"],
                keywords=d["title_keywords"],
                target_date=target_date
            )

            if not found:
                upsert_metric(engine, base_row)
                not_found += 1
                lines.append(
                    f"- {d['drama_name']} ({d['channel_name']}): NOT FOUND for {target_date}"
                )
                continue

            stats = get_video_stats(youtube, found["video_id"])
            if not stats:
                base_row["scrape_status"] = "ERROR"
                base_row["scrape_note"] = "Video found but videos.list returned empty"
                upsert_metric(engine, base_row)
                errors += 1
                lines.append(f"- {d['drama_name']} ({d['channel_name']}): ERROR (no stats) {target_date}")
                continue

            base_row.update(stats)
            base_row["scrape_status"] = "FOUND"
            upsert_metric(engine, base_row)
            ok += 1
            lines.append(
                f"- {d['drama_name']} ({d['channel_name']}): FOUND | views={stats['views']} likes={stats['likes']} comments={stats['comments']} | {stats['video_url']}"
            )

        except Exception as e:
            base_row["scrape_status"] = "ERROR"
            base_row["scrape_note"] = str(e)[:950]
            upsert_metric(engine, base_row)
            errors += 1
            lines.append(f"- {d['drama_name']} ({d['channel_name']}): ERROR {target_date} | {e}")

    # email report
    subject = f"YouTube drama scrape report - target {target_date}"
    body = "\n".join([
        f"Target date: {target_date}",
        f"Results: FOUND={ok}, NOT_FOUND={not_found}, ERROR={errors}",
        "",
        "Details:",
        *lines
    ])

    if SMTP_USER and SMTP_PASS and REPORT_TO:
        send_report(SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, REPORT_TO, subject, body)

    return {"found": ok, "not_found": not_found, "errors": errors, "lines": lines}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Target date (YYYY-MM-DD). If omitted, uses (LK today - 7 days).")
    args = parser.parse_args()

    if args.date:
        target_date = datetime.strptime(args.date, "%Y-%m-%d").date()
    else:
        target_date = lk_today_date() - timedelta(days=7)

    run_for_date(target_date)

if __name__ == "__main__":
    main()