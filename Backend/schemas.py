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

class StudentUpdate(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[EmailStr] = None
    college: Optional[str] = None
    degree:Optional[str] = None
    department: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None
    password: Optional[str] = None

class OrganizerCreate(BaseModel):
    name : str
    organizer_id : str
    number : str
    email : EmailStr
    college : str
    department : str
    role : str
    club : Optional[str]=None
    password : str = Field(min_length=6 , max_length=20)
    

class EventCreate(BaseModel):
    event_name : str
    category : str
    college : str
    location : str
    event_date :datetime
    organizer_id  : int
    coordinator_name : str
    coordinator_number : str
    coordinator_email : EmailStr
    description : Optional[str] = None
    entry_fee : Optional[int] = None
    poster_url : Optional[str] = None
    registration_link : Optional[str] = None
    max_participants : Optional[int] = 500


class OTPRequest(BaseModel):
    email: str
    user_id: str
    role: str

class OTPVerify(BaseModel):
    email: str
    user_id: str
    role: str
    otp: str

class ResetPassword(BaseModel):
    email: str
    user_id: str
    role: str
    new_password: str

class EventUpdate(BaseModel):
    event_name: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    college: Optional[str] = None
    location: Optional[str] = None
    event_date: Optional[datetime] = None
    coordinator_name: Optional[str] = None
    coordinator_number: Optional[str] = None
    coordinator_email: Optional[EmailStr] = None
    entry_fee: Optional[int] = None
    poster_url: Optional[str] = None
    registration_link: Optional[str] = None
    max_participants: Optional[int] = None

class RegistrationCreate(BaseModel):
    user_id: int
    event_id: int