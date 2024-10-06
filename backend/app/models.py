from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime, timezone

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    event = Column(String(255), nullable=False)
    user = Column(String(255))
    ip = Column(String(100))
    site_url = Column(String(255))
    url = Column(Text)
    method = Column(String(10))
    user_agent = Column(Text)
    referrer = Column(Text)
    query_string = Column(Text)
    remote_addr = Column(String(100))
    request_time = Column(Integer)
    extra = Column(Text)
