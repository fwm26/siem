from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Pydantic model for creating a log
class LogCreate(BaseModel):
    event: str
    user: Optional[str] = None
    ip: Optional[str] = None
    site_url: Optional[str] = None
    url: Optional[str] = None
    method: Optional[str] = None
    user_agent: Optional[str] = None
    referrer: Optional[str] = None
    query_string: Optional[str] = None
    remote_addr: Optional[str] = None
    request_time: Optional[int] = None
    extra: Optional[str] = None

# Pydantic model for the response (including timestamp and ID)
class Log(BaseModel):
    id: int
    timestamp: datetime
    event: str
    user: Optional[str] = None
    ip: Optional[str] = None
    site_url: Optional[str] = None
    url: Optional[str] = None
    method: Optional[str] = None
    user_agent: Optional[str] = None
    referrer: Optional[str] = None
    query_string: Optional[str] = None
    remote_addr: Optional[str] = None
    request_time: Optional[int] = None
    extra: Optional[str] = None

    class Config:
        orm_mode = True
