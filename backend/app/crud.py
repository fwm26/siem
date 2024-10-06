from sqlalchemy.orm import Session
from .models import User, Log
from .schemas import UserCreate, LogCreate
import bcrypt
from datetime import datetime

# Fetch a user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Create a new user in the database
def create_user(db: Session, user: UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())  # Proper bcrypt hashing
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password.decode('utf-8')  # Store the hashed password as a string
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Fetch a user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Authenticate user during login
def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        return False
    return user

def create_log(db: Session, log: LogCreate):
    # If no timestamp is provided, use the current time
    if log.timestamp is None:
        log.timestamp = datetime.utcnow()

    # Create a new log record
    new_log = Log(
        timestamp=log.timestamp,
        event=log.event,
        user=log.user,
        ip=log.ip,
        site_url=log.site_url,
        url=log.url,
        method=log.method,
        user_agent=log.user_agent,
        referrer=log.referrer,
        query_string=log.query_string,
        remote_addr=log.remote_addr,
        request_time=log.request_time,
        extra=log.extra
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log