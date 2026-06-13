from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

# Users
@router.post("/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/", response_model=list[schemas.UserRead])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

# Emails
@router.post("/{user_id}/emails", response_model=schemas.EmailRead)
def add_email(user_id: int, email: schemas.EmailCreate, db: Session = Depends(get_db)):
    return crud.create_email(db, user_id, email)

@router.get("/{user_id}/emails", response_model=list[schemas.EmailRead])
def list_emails(user_id: int, db: Session = Depends(get_db)):
    return crud.get_emails(db, user_id)