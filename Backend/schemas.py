from pydantic import BaseModel, EmailStr , Field
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    full_name: str
    student_id: str
    phone_number: str
    email: EmailStr
    college: str
    department: str
    password: str = Field(min_length=6, max_length=72)

class Login(BaseModel):
    identifier: str   # can be email OR roll number
    password: str



class OrganizerCreate(BaseModel):
    name : str
    organizer_id : str
    number : str
    email : EmailStr
    college : str
    department : str
    club : Optional[str]=None
    role : str
    password : str = Field(min_length=6 , max_length=20)
    

class EventCreate(BaseModel):
    event_name : str
    category : str
    description : Optional[str] = None
    college : str
    location : str
    event_date :datetime
    organizer_id  : int
    coordinator_name : str
    coordinator_number : str
    coordinator_email : EmailStr
    entry_fee : Optional[int] = None
    poster_url : Optional[str] = None
    registration_link : Optional[str] = None
    max_participants : Optional[int] = 500


