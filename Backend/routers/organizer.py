from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session 
from database import SessionLocal
import models
import schemas
from typing import Optional
from passlib.context import CryptContext
from sqlalchemy import or_

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"] , deprecated = "auto")

# Database Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#-------------------------
# Organizer Registration
#-------------------------

@router.post("/Organizer_register")
async def create_organizer(organizer : schemas.OrganizerCreate , db:Session=Depends(get_db)):
    email_existing = db.query(models.Organizer).filter(
        models.Organizer.email == organizer.email
    ).first()
    if email_existing :
        raise HTTPException(status_code=400 ,detail="Email already Existed")
    
    existing_id = db.query(models.Organizer).filter(
        models.Organizer.organizer_id == organizer.organizer_id
    ).first()

    if existing_id :
        raise HTTPException(status_code=404 , detail = "Organizer ID is already Existed")

    hash_password = pwd_context.hash(organizer.password)

    new_organizer = models.Organizer(
        name = organizer.name,
        organizer_id = organizer.organizer_id,
        number = organizer.number,
        email = organizer.email,
        college = organizer.college,
        department = organizer.department,
        club = organizer.club,
        role = organizer.role,
        password = hash_password
    )
    db.add(new_organizer)
    db.commit()
    db.refresh(new_organizer)

    return{
        "message":"Organizer created successfully",
        "organizer":new_organizer
    }

#-----------------------
# Get All Organizers
#-----------------------
@router.get("/organizers")
def get_organizers(db: Session = Depends(get_db)):
    return db.query(models.Organizer).all()

#-----------------------
# Get  Organizer By ID
#-----------------------
@router.get("/organizers/{id}")
def get_organizer(id: int, db: Session = Depends(get_db)):
    organizer = db.query(models.Organizer).filter(models.Organizer.id == id).first()

    if not organizer:
        raise HTTPException(status_code=404, detail="Organizer not found")

    return organizer


#------------------
# Organizer Login
#-----------------

@router.post("/organizer_login")
def login(user : schemas.Login , db : Session = Depends(get_db)):
    db_user = db.query(models.Organizer).filter(
        or_(
            models.Organizer.email == user.identifier,
            models.Organizer.organizer_id == user.identifier
        )
    ).first()
    if not db_user : 
        raise HTTPException(status_code=400 , detail="Invalid Email or Organiser_id")

    if not pwd_context.verify( user.password , db_user.password ):
        raise HTTPException(status_code=400 , detail = "Invalid Password")
    
    return{
        "message" : "Organizer login Successfully",
        "id" : db_user.id,
        "FullName" : db_user.name
    }


