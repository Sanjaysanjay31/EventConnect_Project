from sqlalchemy import Column, Integer, String , Float , DateTime , ForeignKey
from sqlalchemy.orm import declarative_base , relationship
from datetime import datetime , timezone

# Base for models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    student_id = Column(String, unique=True, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    college = Column(String, nullable=False)
    department = Column(String, nullable=False)
    bio = Column(String, nullable=True)
    degree = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)
    github = Column(String, nullable=True)
    portfolio = Column(String, nullable=True)
    image = Column(String , nullable=True)
    hashed_password = Column(String, nullable=False)


class Organizer(Base):
    __tablename__ = "organizers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    organizer_id = Column(String, nullable=False)
    number = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    college = Column(String, nullable=False)
    department = Column(String , nullable=True )
    bio = Column(String , nullable=True)
    linkedin = Column(String, nullable=True)
    github = Column(String, nullable=True)
    image = Column(String , nullable=True)
    club = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String , nullable=False)
    status = Column(String, default="Pending")
    created_at = Column(DateTime , default=lambda : datetime.now(timezone.utc))

    events = relationship("Event",back_populates="organizers")

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String(200), nullable=False, index=True)
    category = Column(String(100), nullable=False)
    description = Column(String)
    college = Column(String(200), nullable=False)
    location = Column(String(200), nullable=False)
    event_date = Column(DateTime, nullable=False)

    organizer_id = Column(Integer, ForeignKey("organizers.id"))

    organizer_name = Column(String(150), nullable=False)
    organizer_number = Column(String(15), nullable=False)
    organizer_email = Column(String(150), nullable=False)
    coordinator_name = Column(String(150), nullable=False)
    coordinator_number = Column(String(15), nullable=False)
    coordinator_email = Column(String(150), nullable=False)
    entry_fee = Column(Integer, nullable=True)
    poster_url = Column(String(500))
    registration_link = Column(String)
    max_participants = Column(Integer , default=500 )
    registered_participants = Column(Integer, default=0, nullable=False)
    status = Column(String, default="upcoming")
    approval = Column(String , default="Pending")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    organizers = relationship("Organizer", back_populates="events")

