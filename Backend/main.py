from fastapi import FastAPI
from database import engine
import models
from fastapi.middleware.cors import CORSMiddleware

from routers import student_module ,events , organizer

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["event-connect-project.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_module.router)
app.include_router(organizer.router)
app.include_router(events.router)
