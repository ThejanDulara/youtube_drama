from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

def get_engine(db_url: str) -> Engine:
    # pool_pre_ping helps keep Railway MySQL connections healthy
    return create_engine(db_url, pool_pre_ping=True, pool_recycle=300)

UPSERT_SQL = """
INSERT INTO youtube_episode_metrics (
  drama_key, drama_name, episode_number,
  channel_key, channel_name, channel_id,
  target_date, schedule_type,
  video_id, video_title, video_url, video_published_at,
  views, likes, comments,
  scrape_status, scrape_note,
  created_at
)
VALUES (
  :drama_key, :drama_name, :episode_number,
  :channel_key, :channel_name, :channel_id,
  :target_date, :schedule_type,
  :video_id, :video_title, :video_url, :video_published_at,
  :views, :likes, :comments,
  :scrape_status, :scrape_note,
  NOW()
)
ON DUPLICATE KEY UPDATE
  episode_number=VALUES(episode_number),
  video_id=VALUES(video_id),
  video_title=VALUES(video_title),
  video_url=VALUES(video_url),
  video_published_at=VALUES(video_published_at),
  views=VALUES(views),
  likes=VALUES(likes),
  comments=VALUES(comments),
  scrape_status=VALUES(scrape_status),
  scrape_note=VALUES(scrape_note),
  created_at=NOW();
"""

def upsert_metric(engine: Engine, row: dict) -> None:
    with engine.begin() as conn:
        conn.execute(text(UPSERT_SQL), row)