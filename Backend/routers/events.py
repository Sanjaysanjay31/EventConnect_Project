from fastapi import HTTPException , APIRouter , Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Event Create 

@router.post("/CreateEvent")
def CreateEvent(event: schemas.EventCreate, db: Session = Depends(get_db)):

    existing_event = db.query(models.Event).filter(
        models.Event.event_name == event.event_name,
        models.Event.college == event.college
    ).first()

    if existing_event:
        raise HTTPException(
            status_code=400,
            detail="Event name already exists in this college"
        )

    organizer_c = db.query(models.Organizer).filter(
        models.Organizer.id == event.organizer_id
    ).first()

    if not organizer_c :
        raise HTTPException(status_code=404 , detail="Organizer not found")

    new_event = models.Event(
        event_name=event.event_name,
        category=event.category,
        description=event.description,
        college=event.college,
        location=event.location,
        event_date=event.event_date,
        
        organizer_id=organizer_c.id,
        organizer_name=organizer_c.name,
        organizer_number=organizer_c.number,
        organizer_email=organizer_c.email,

        coordinator_name=event.coordinator_name,
        coordinator_number=event.coordinator_number,
        coordinator_email=event.coordinator_email,
        entry_fee=event.entry_fee,
        poster_url=event.poster_url,
        registration_link=event.registration_link,
        max_participants=event.max_participants
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