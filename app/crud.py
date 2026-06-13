from sqlalchemy.orm import Session
from app import models, schemas
from passlib.hash import bcrypt

# Users
def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = bcrypt.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Emails
def create_email(db: Session, user_id: int, email: schemas.EmailCreate):
    db_email = models.Email(email=email.email, user_id=user_id)
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email

def get_emails(db: Session, user_id: int):
    return db.query(models.Email).filter(models.Email.user_id == user_id).all()