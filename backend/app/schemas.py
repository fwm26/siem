import re
from pydantic import BaseModel, EmailStr, validator, Field
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

    class Config:
        from_attributes = True  # This enables SQLAlchemy model compatibility for Pydantic v2


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
        from_attributes = True  # Use 'from_attributes' for Pydantic v2 compatibility with SQLAlchemy


# Model for users
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

    class Config:
        from_attributes = True  # Compatibility with SQLAlchemy for Pydantic v2


class UserCreate(UserBase):
    password: str

    # Password validation (min 8 chars, at least one uppercase, and one special character)
    @validator('password')
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[\W_]', value):  # Special characters check
            raise ValueError('Password must contain at least one special character')
        return value


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True  # Compatibility with SQLAlchemy for Pydantic v2


# Token models
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
