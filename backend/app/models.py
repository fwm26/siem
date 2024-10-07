from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone



Base = declarative_base()

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    event = Column(String(255))
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


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    email = Column(String(255))
    full_name = Column(String(255))
    hashed_password = Column(String(255))
    disabled = Column(String(255))
