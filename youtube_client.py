import re
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone

def yt_build(api_key: str):
    return build("youtube", "v3", developerKey=api_key, cache_discovery=False)

def normalize(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())

def date_variants(target_date):
    d = target_date
    day = d.day
    month_name = d.strftime("%B")
    year = d.year

    def ordinal(n):
        if 10 <= n % 100 <= 20:
            suf = "th"
        else:
            suf = {1:"st",2:"nd",3:"rd"}.get(n % 10, "th")
        return f"{n}{suf}"

    return [
        d.strftime("%Y-%m-%d"),
        f"{ordinal(day)} {month_name} {year}",
        f"{day} {month_name} {year}",
        d.strftime("%d/%m/%Y"),
        d.strftime("%d-%m-%Y"),
    ]

def find_video_for_date(youtube, channel_id: str, keywords: list[str], target_date):
    # Define publish window (±1 day buffer)
    start_dt = datetime.combine(target_date - timedelta(days=1), datetime.min.time()).replace(tzinfo=timezone.utc)
    end_dt = datetime.combine(target_date + timedelta(days=1), datetime.max.time()).replace(tzinfo=timezone.utc)

    resp = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        order="date",
        type="video",
        publishedAfter=start_dt.isoformat().replace("+00:00", "Z"),
        publishedBefore=end_dt.isoformat().replace("+00:00", "Z"),
        q=" ".join(keywords)
    ).execute()

    variants = [normalize(v) for v in date_variants(target_date)]
    kw_norms = [normalize(k) for k in keywords]

    for item in resp.get("items", []):
        sn = item.get("snippet", {})
        title = sn.get("title", "")
        title_n = normalize(title)

        # Must contain drama keyword
        if not any(k in title_n for k in kw_norms):
            continue

        # Must contain exact target date
        if not any(v in title_n for v in variants):
            continue

        return {
            "video_id": item["id"]["videoId"],
            "title": title,
            "publishedAt": sn.get("publishedAt"),
        }

    return None

def extract_episode_number(title: str):
    if not title:
        return None
    m = re.search(r"episode\s*(\d+)", title, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None

def get_video_stats(youtube, video_id: str):
    resp = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    ).execute()

    items = resp.get("items", [])
    if not items:
        return None

    it = items[0]
    stats = it.get("statistics", {})
    sn = it.get("snippet", {})

    published_at = sn.get("publishedAt")
    published_dt = None
    if published_at:
        published_dt = datetime.fromisoformat(published_at.replace("Z", "+00:00")).astimezone(timezone.utc)

    def to_int(x):
        try:
            return int(x)
        except:
            return None

    title = sn.get("title")

    return {
        "video_id": video_id,
        "video_title": title,
        "episode_number": extract_episode_number(title),
        "video_url": f"https://www.youtube.com/watch?v={video_id}",
        "video_published_at": published_dt.strftime("%Y-%m-%d %H:%M:%S") if published_dt else None,
        "views": to_int(stats.get("viewCount")),
        "likes": to_int(stats.get("likeCount")),
        "comments": to_int(stats.get("commentCount")),
    }

