import json
from fastapi import FastAPI
from starlette.responses import Response
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import List
from pydantic import BaseModel

app = FastAPI()

@app.get("/hello")
def hello():
        return Response(content=f"Hello world", status_code=200)

@app.get("/welcome")
def welcoming(request: Request, name: str = "Undefined"):
    return Response(content=f"Welcome {name}", status_code=200)

class StudentModel(BaseModel):
    Reference: str
    FirstName: str
    LastName: str
    age: int

student_data: List[StudentModel] = []

def serialized_stored_student():
    student_converted = []
    for student in student_data:
        student_converted.append(student.model_dump())
    return student_converted

@app.get("/students")
def list_students():
    return serialized_stored_student()

@app.post("/students")
def add_student(new_student: StudentModel):
    student_data.append(new_student)
        return student_data

@app.put("/students")
def edit_data(data: StudentModel):
    update = False
    for student in student_data:
        if data.Reference == student:
            student = data
            update = True
    if not update:
        return add_student(StudentModel)
    return Response(content=html_content, status_code=200)

