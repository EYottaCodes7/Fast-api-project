from fastapi import FastAPI
from app.routers import users
from app.database import Base, engine
import app.models

# Ensure tables exist (just in case)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API is working"}