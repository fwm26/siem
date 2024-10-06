from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime, timezone

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    event = Column(String(255), nullable=False)
    user = Column(String(255), nullable=True)
    ip = Column(String(100), nullable=True)
    site_url = Column(String(255), nullable=True)
    url = Column(Text, nullable=True)
    method = Column(String(10), nullable=True)
    user_agent = Column(Text, nullable=True)
    referrer = Column(Text, nullable=True)
    query_string = Column(Text, nullable=True)
    remote_addr = Column(String(100), nullable=True)
    request_time = Column(Integer, nullable=True)
    extra = Column(Text, nullable=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)