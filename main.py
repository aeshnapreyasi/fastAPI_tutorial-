from fastapi import FastAPI #core framework to build api
from pydantic import BaseModel # helps for validation 
from typing import List 

app = FastAPI()

class Student(BaseModel):
    id: int 
    name: str 
    origin: str 

studentArr: List[Student] = []

#decorators 
@app.get("/")
def read_root():
    return {"message": "Welcome to Student Library"}

@app.get("/studentArr") #decorator 
def get_student():
    return studentArr

@app.post("/studentArr")
def add_student(student: Student):
    studentArr.append(student)
    return student 

@app.put("/studentArr/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(studentArr):
        if student.id == student_id:
            studentArr[index] = update_student
            return update_student
    return {"error": "Student not found"}

@app.delete("/studentArr/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(studentArr):
        if student.id == student_id:
            deleted = studentArr.pop(index)
            return deleted 
    return {"error": "Student not found"}