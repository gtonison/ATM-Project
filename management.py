from fastapi import FastAPI , HTTPException
from pydantic import BaseModel ,Field

app = FastAPI()
students ={}

class Student(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(ge=5)
    course: str
    reg_no: int

@app.post("/students/{student_id}", status_code=201)
def add_student(student_id: int,student: Student):
    students[student_id] = student.model_dump()
    return student

@app.get("/students/{school_record}")
def get_student(student_id: int, student: Student):
    if student not in students:
     raise HTTPException(status_code=409 , detail= "record not found in the system")

    return students[student_id]

@app.put("/students/{school_record}")
def update(student_id: int,student: Student):
    if student_id not in students:
        raise HTTPException(status_code= 409 , detail="record already exists")
    students[student_id] = {"name": name, age: int , reg_no: int}
    return {"message":"successfully updated it"}


@app.get("/students/{school_register}")
def list_all_students(student_id: int, student: Student):
    return students[student_id]

@app.delete("/students/{school_record}")
def delete_student(student_id: int, student: Student):
   if student_id in students:
       if student_id not in students:
           raise HTTPException(status_code=409 ,detail=" record not found")
       del students[student_id]
       return {"message":"student has been deleted successfully"}