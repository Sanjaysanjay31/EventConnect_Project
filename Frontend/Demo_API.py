from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

data = {}

@app.post("/create_user/{user_id}")
async def create_user(user_id : int) :
    if user_id in data :
        return{"Error" :"User is already in data"}
    else :
        data[user_id]= { "Name":"Sanjay" , "Phone" : 898806254 , "Student_id":"24B11DS095"}
        return{"User created Successfully"}
    

@app.put("/update/{user_id}")
def update(user_id : int ) :
    if user_id not in data :
        return {"Error" : "User is not found in data "}
    else :
        data[user_id]={
            "Name":"Sanju" ,
            "Phone" : 9948806254 ,
            "Student_id":"24B11DS095"
        }
        return {"message": "User updated successfully"}


@app.get("/details/{user_id}")
def details(user_id : int) :
    if user_id not in data :
        return{"Error":"User is not found in data "}
    else :
        return data[user_id]
    

@app.delete("/delete/{user_id}")
def delete(user_id : int ):
    if user_id in data:
        del data[user_id]
        return {"message" : "User deleted successfully"}
    else :
        return {"message" : "User not found in data "}
        
    
class Event(BaseModel):
    title : str
    id : int
    event_type : str
    location : str
    date : str

@app.post("/events")
async def create_event(event : Event):
    return event



