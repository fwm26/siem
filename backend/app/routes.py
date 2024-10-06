from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

router = APIRouter()

# Create a log entry
@router.post("/logs/", response_model=schemas.Log)
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    new_log = models.Log(**log.dict())
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

# Get all logs
@router.get("/logs/", response_model=List[schemas.Log])
def get_logs(db: Session = Depends(get_db)):
    return db.query(models.Log).all()

# Get a log by ID
@router.get("/logs/{log_id}", response_model=schemas.Log)
def get_log(log_id: int, db: Session = Depends(get_db)):
    log = db.query(models.Log).filter(models.Log.id == log_id).first()
    if log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return log
