from fastapi import HTTPException , APIRouter , Depends, Form, File, UploadFile
from sqlalchemy.orm import Session
from database import SessionLocal, supabase, SUPABASE_URL
import models
import schemas
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Event Create 

@router.post("/CreateEvent")
async def CreateEvent(
    event_name: str = Form(...),
    category: str = Form(...),
    description: str = Form(None),
    college: str = Form(...),
    location: str = Form(...),
    event_date: str = Form(...),
    organizer_id: int = Form(...),
    coordinator_name: str = Form(...),
    coordinator_number: str = Form(...),
    coordinator_email: str = Form(...),
    entry_fee: int = Form(None),
    max_participants: int = Form(...),
    registration_link: str = Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):

    existing_event = db.query(models.Event).filter(
        models.Event.event_name == event_name,
        models.Event.college == college
    ).first()

    if existing_event:
        raise HTTPException(
            status_code=400,
            detail="Event name already exists in this college"
        )

    organizer_c = db.query(models.Organizer).filter(
        models.Organizer.id == organizer_id
    ).first()

    if not organizer_c :
        raise HTTPException(status_code=404 , detail="Organizer not found")

    poster_url = None
    if image:
        try:
            file_bytes = await image.read()
            file_name = f"event_{uuid.uuid4()}.jpg"

            supabase.storage.from_("Profile_Images").upload(
                file_name,
                file_bytes,
                {"content-type": image.content_type}
            )
            poster_url = f"{SUPABASE_URL}/storage/v1/object/public/Profile_Images/{file_name}"
        except Exception as e:
            print("Image Upload Error:", e)
            raise HTTPException(status_code=500, detail="Image upload failed")

    new_event = models.Event(
        event_name=event_name,
        category=category,
        description=description,
        college=college,
        location=location,
        event_date=event_date,
        
        organizer_id=organizer_c.id,
        organizer_name=organizer_c.name,
        organizer_number=organizer_c.number,
        organizer_email=organizer_c.email,

        coordinator_name=coordinator_name,
        coordinator_number=coordinator_number,
        coordinator_email=coordinator_email,
        entry_fee=entry_fee,
        poster_url=poster_url,
        registration_link=registration_link,
        max_participants=max_participants
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return {
        "message": "Event created successfully",
        "event_id": new_event.id
    }



# -----------------------------
# Get All Events
# -----------------------------
@router.get("/events")
def get_events(db: Session = Depends(get_db)):

    events = db.query(models.Event).all()

    if not events:
        raise HTTPException(
            status_code=404,
            detail="No events found"
        )

    return events


# -----------------------------
# Get Single Event
# -----------------------------
@router.get("/events/{id}")
def get_event(id: int, db: Session = Depends(get_db)):

    event = db.query(models.Event).filter(
        models.Event.id == id
    ).first()

    if not event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )

    return event


# -----------------------------
# Update Event
# -----------------------------
@router.put("/events/{id}")
async def update_event(
    id: int, 
    event_name: str = Form(None),
    category: str = Form(None),
    description: str = Form(None),
    college: str = Form(None),
    location: str = Form(None),
    event_date: str = Form(None),
    coordinator_name: str = Form(None),
    coordinator_number: str = Form(None),
    coordinator_email: str = Form(None),
    entry_fee: int = Form(None),
    max_participants: int = Form(None),
    registration_link: str = Form(None),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):

    db_event = db.query(models.Event).filter(
        models.Event.id == id
    ).first()

    if not db_event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )
    
    if image:
        try:
            file_bytes = await image.read()
            file_name = f"event_{id}_{uuid.uuid4()}.jpg"

            supabase.storage.from_("Profile_Images").upload(
                file_name,
                file_bytes,
                {"content-type": image.content_type}
            )
            db_event.poster_url = f"{SUPABASE_URL}/storage/v1/object/public/Profile_Images/{file_name}"
        except Exception as e:
            print("Image Upload Error:", e)
            raise HTTPException(status_code=500, detail="Image upload failed")
            
    if event_name is not None: db_event.event_name = event_name
    if category is not None: db_event.category = category
    if description is not None: db_event.description = description
    if college is not None: db_event.college = college
    if location is not None: db_event.location = location
    if event_date is not None: db_event.event_date = event_date
    if coordinator_name is not None: db_event.coordinator_name = coordinator_name
    if coordinator_number is not None: db_event.coordinator_number = coordinator_number
    if coordinator_email is not None: db_event.coordinator_email = coordinator_email
    if entry_fee is not None: db_event.entry_fee = entry_fee
    if max_participants is not None: db_event.max_participants = max_participants
    if registration_link is not None: db_event.registration_link = registration_link
    
    db.commit()
    db.refresh(db_event)
    return {"message": "Event updated successfully", "event": db_event}


# -----------------------------
# Delete Event
# -----------------------------
@router.delete("/events/{id}")
def delete_event(id: int, db: Session = Depends(get_db)):

    db_event = db.query(models.Event).filter(
        models.Event.id == id
    ).first()

    if not db_event:
        raise HTTPException(
            status_code=404,
            detail="Event not found"
        )
    
    # Ensure associated registrations are deleted to prevent foreign key violation
    db.query(models.Registration).filter(models.Registration.event_id == id).delete(synchronize_session=False)
    
    db.delete(db_event)
    db.commit()
    return {"message": "Event deleted successfully"}


# -----------------------------
# Get Organizer Events
# -----------------------------
@router.get("/organizer/{organizer_id}/events")
def get_organizer_events(organizer_id: int, db: Session = Depends(get_db)):

    events = db.query(models.Event).filter(
        models.Event.organizer_id == organizer_id
    ).all()

    if not events:
        raise HTTPException(
            status_code=404,
            detail="No events found for this organizer"
        )

    return events

# -----------------------------
# Register for an Event
# -----------------------------
@router.post("/events/{id}/register")
def register_event(id: int, reg_data: schemas.RegistrationCreate, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
        
    user = db.query(models.User).filter(models.User.id == reg_data.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    existing = db.query(models.Registration).filter(
        models.Registration.user_id == user.id,
        models.Registration.event_id == event.id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already registered for this event")
        
        
    new_reg = models.Registration(
        user_id=user.id,
        event_id=event.id,
        student_name=user.full_name,
        student_roll=user.student_id,
        student_phone=user.phone_number,
        student_email=user.email,
        student_college=user.college,
        student_department=user.department,
        event_name=event.event_name,
        event_category=event.category
    )
    event.registered_participants += 1
    db.add(new_reg)
    db.commit()
    return {"message": "Successfully registered"}

# -----------------------------
# Get Participants for Organizer
# -----------------------------
@router.get("/organizer/{organizer_id}/participants")
def get_participants(organizer_id: int, db: Session = Depends(get_db)):
    events = db.query(models.Event).filter(models.Event.organizer_id == organizer_id).all()
    event_ids = [e.id for e in events]
    
    if not event_ids:
        return []
        
    registrations = db.query(models.Registration).filter(models.Registration.event_id.in_(event_ids)).all()
    
    results = []
    for reg in registrations:
        user = reg.user
        event = reg.event
        results.append({
            "registration_id": reg.id,
            "registered_at": reg.registered_at,
            "status": reg.status,
            "user_id": user.id,
            "name": user.full_name,
            "student_id": user.student_id,
            "phone": user.phone_number,
            "email": user.email,
            "college": user.college,
            "department": user.department,
            "event_id": event.id,
            "event_name": event.event_name,
            "category": event.category
        })
        
    return results

# -----------------------------
# Get User Registrations
# -----------------------------
@router.get("/user/{user_id}/registrations")
def get_user_registrations(user_id: int, db: Session = Depends(get_db)):
    registrations = db.query(models.Registration).filter(models.Registration.user_id == user_id).all()
    results = []
    for reg in registrations:
        # Get event date if possible
        event = db.query(models.Event).filter(models.Event.id == reg.event_id).first()
        event_date = event.event_date if event else None
        
        results.append({
            "registration_id": reg.id,
            "event_id": reg.event_id,
            "event_name": reg.event_name,
            "category": reg.event_category,
            "status": reg.status,
            "registered_at": reg.registered_at,
            "event_date": event_date
        })
    return results
