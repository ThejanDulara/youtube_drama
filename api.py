from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, jsonify
from sqlalchemy import text

from config import DATABASE_URL
from db import get_engine

app = Flask(__name__)
engine = get_engine(DATABASE_URL)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/api/metrics")
def metrics():
    drama_key = request.args.get("drama_key")
    start = request.args.get("start")  # YYYY-MM-DD
    end = request.args.get("end")      # YYYY-MM-DD

    where = []
    params = {}

    if drama_key:
        where.append("drama_key = :drama_key")
        params["drama_key"] = drama_key
    if start:
        where.append("target_date >= :start")
        params["start"] = start
    if end:
        where.append("target_date <= :end")
        params["end"] = end

    where_sql = ("WHERE " + " AND ".join(where)) if where else ""

    q = f"""
    SELECT
      drama_key, drama_name, episode_number,
      channel_key, channel_name,
      target_date,
      video_id, video_title, video_url, video_published_at,
      views, likes, comments,
      scrape_status, scrape_note,
      created_at
      FROM youtube_episode_metrics
      {where_sql}
      ORDER BY target_date DESC, drama_key ASC
      LIMIT 5000
    """

    with engine.begin() as conn:
        rows = conn.execute(text(q), params).mappings().all()
    return jsonify([dict(r) for r in rows])