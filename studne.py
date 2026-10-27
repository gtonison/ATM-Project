from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {}

@app.post("/students")
def add_student(student_id: int, name: str, age: int, course: str):

    if student_id in students:
        raise HTTPException(
            status_code=409,
            detail="A student with this ID already exists"
        )

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course
    }

    return {
        "message": "Student registered successfully",
        "student": students[student_id]
    }


@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    name: str,
    age: int,
    course: str
):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course
    }

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]

    return {
        "message": "Student deleted successfully"
    }