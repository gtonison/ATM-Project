from pydantic import BaseModel
from fastapi import FastAPI

class student(BaseModel):
    name = str
    age = int
    
app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id : int):
    return user_id

@app.post("/students")
def create_student():
    return {"message":"student has been created"}
@app.put("student/ "status_code=