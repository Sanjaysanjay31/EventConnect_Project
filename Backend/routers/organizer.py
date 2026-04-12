from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.orm import Session
from database import SessionLocal, supabase, SUPABASE_URL
import models , schemas
from passlib.context import CryptContext
from sqlalchemy import or_
import uuid

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# =========================
# DB
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# REGISTER
# =========================
@router.post("/Organizer_register")
def create_organizer(organizer: schemas.OrganizerCreate, db: Session = Depends(get_db)):

    if db.query(models.Organizer).filter(models.Organizer.email == organizer.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    if db.query(models.Organizer).filter(models.Organizer.organizer_id == organizer.organizer_id).first():
        raise HTTPException(status_code=400, detail="Organizer ID already exists")

    hashed_password = pwd_context.hash(organizer.password)

    new = models.Organizer(
        name=organizer.name,
        organizer_id=organizer.organizer_id,
        number=organizer.number,
        email=organizer.email,
        college=organizer.college,
        department=organizer.department,
        club=organizer.club,
        role=organizer.role,
        password=hashed_password
    )

    db.add(new)
    db.commit()
    db.refresh(new)

    return {
        "message": "Organizer registered successfully",
        "id": new.id,
        "organizer_id": new.organizer_id,
        "email": new.email,
        "role": new.role
    }


# =========================
# LOGIN
# =========================
@router.post("/organizer_login")
def login(user: schemas.Login, db: Session = Depends(get_db)):

    db_user = db.query(models.Organizer).filter(
        or_(
            models.Organizer.email == user.identifier,
            models.Organizer.organizer_id == user.identifier
        )
    ).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")
    
     # 🔴 NEW CONDITION (Pending approval)
    if db_user.status == "Pending":
        raise HTTPException(status_code=403, detail="Wait for Admin Approval")

    # ❌ Optional: Rejected case
    if db_user.status == "Rejected":
        raise HTTPException(status_code=403, detail="Your account was rejected by admin")

 
    return {
        "message": "Login successful",
        "id": db_user.id,
        "name": db_user.name,
        "email": db_user.email,
        "role": db_user.role,
        "organizer_id": db_user.organizer_id
    }


# =========================
# GET ORGANIZER
# =========================
@router.get("/get-organizer/{id}")
def get_organizer(id: int, db: Session = Depends(get_db)):

    user = db.query(models.Organizer).filter(models.Organizer.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Organizer not found")

    return {
        "id": user.id,
        "name": user.name,
        "user_id": user.organizer_id,
        "phone": user.number,
        "email": user.email,
        "college": user.college,
        "department": user.department,
        "club": user.club,
        "role": user.role,
        "bio": user.bio or "",
        "linkedin": user.linkedin or "",
        "github": user.github or "",
        "image": user.image or ""
    }


#--------------------
# Update Organizer Profile
#--------------------
@router.patch("/update-organizer/{id}")
async def update_organizer(
    id: int,
    name: str = Form(None),
    phone: str = Form(None),
    email: str = Form(None),
    college: str = Form(None),
    department: str = Form(None),
    club: str = Form(None),
    role: str = Form(None),
    bio: str = Form(None),
    linkedin: str = Form(None),
    github: str = Form(None),

    # 🔐 Password fields
    current_password: str = Form(None),
    new_password: str = Form(None),

    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    # =========================
    # 🔍 Get Organizer
    # =========================
    user = db.query(models.Organizer).filter(models.Organizer.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Organizer not found")

    # =========================
    # ✅ Email Check
    # =========================
    if email:
        existing = db.query(models.Organizer).filter(models.Organizer.email == email).first()
        if existing and existing.id != id:
            raise HTTPException(status_code=400, detail="Email already in use")

    # =========================
    # 🔐 Password Update
    # =========================
    if current_password or new_password:

        if not (current_password and new_password):
            raise HTTPException(status_code=400, detail="Both passwords required")

        # ✅ Verify current password
        if not pwd_context.verify(current_password, user.password):
            raise HTTPException(status_code=400, detail="Current password is incorrect")

        # ✅ Validate new password
        if len(new_password) < 6:
            raise HTTPException(status_code=400, detail="Password must be at least 6 characters")

        # ✅ Update password
        user.password = pwd_context.hash(new_password)

    # =========================
    # 🖼️ Image Upload
    # =========================
    if image:
        try:
            file_bytes = await image.read()
            file_name = f"{id}_{uuid.uuid4()}.jpg"

            supabase.storage.from_("Profile_Images").upload(
                file_name,
                file_bytes,
                {"content-type": image.content_type}
            )

            user.image = f"{SUPABASE_URL}/storage/v1/object/public/Profile_Images/{file_name}"

        except Exception as e:
            print("Image Upload Error:", e)
            raise HTTPException(status_code=500, detail="Image upload failed")

    # =========================
    # ✏️ Update Fields
    # =========================
    if name: user.name = name
    if phone: user.number = phone
    if email: user.email = email
    if college: user.college = college
    if department: user.department = department
    if club: user.club = club
    if role: user.role = role
    if bio: user.bio = bio
    if linkedin: user.linkedin = linkedin
    if github: user.github = github

    # =========================
    # 💾 Save Changes
    # =========================
    db.commit()
    db.refresh(user)

    return {
        "message": "Organizer updated successfully",
        "image": user.image
    }