from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes import router

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include your API routes
app.include_router(router)
