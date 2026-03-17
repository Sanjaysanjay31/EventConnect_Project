from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas
from passlib.context import CryptContext
from sqlalchemy import or_

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Student registration form 

@router.post("/Student_register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    if db.query(models.User).filter(models.User.student_id == user.student_id).first():
        raise HTTPException(status_code=400, detail="Student ID already exists")

    hashed_password = pwd_context.hash(user.password)

    new_user = models.User(
        full_name=user.full_name,
        student_id=user.student_id,
        phone_number=user.phone_number,
        email=user.email,
        college=user.college,
        department=user.department,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "student_id": new_user.id
    }

# Student Login

@router.post("/Student_login")
def login(user: schemas.Login, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(
        or_(
            models.User.email == user.identifier,
            models.User.student_id == user.identifier
        )
    ).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or roll number")

    if not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid password")

    return {
        "message": "Login successful",
        "id": db_user.id,
        "full_name": db_user.full_name
    }