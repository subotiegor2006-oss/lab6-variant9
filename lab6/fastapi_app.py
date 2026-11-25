"""FastAPI: Hello + SQLAlchemy CRUD.

Задания: №6 (средняя), №2 и №9 (повышенная).
"""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from lab6.database import Student, get_session, init_db

app = FastAPI(
    title="ЛР №6 — вариант 9",
    description="FastAPI + SQLAlchemy",
    version="1.0.0",
)


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    group: str = Field(..., min_length=1, max_length=20)
    score: float = Field(0.0, ge=0, le=5)


class StudentOut(BaseModel):
    id: int
    name: str
    group: str
    score: float

    model_config = {"from_attributes": True}


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/")
def hello() -> dict:
    """Hello World (задание №6)."""
    return {"message": "Привет FastAPI!"}


@app.get("/students", response_model=List[StudentOut])
def list_students(session: Session = Depends(get_session)):
    """Список всех студентов."""
    return session.query(Student).all()


@app.get("/students/{student_id}", response_model=StudentOut)
def get_student(student_id: int, session: Session = Depends(get_session)):
    """Получить студента по id."""
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    return student


@app.post("/students", response_model=StudentOut, status_code=201)
def create_student(payload: StudentCreate, session: Session = Depends(get_session)):
    """Создать студента."""
    student = Student(name=payload.name, group=payload.group, score=payload.score)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


@app.put("/students/{student_id}", response_model=StudentOut)
def update_student(
    student_id: int,
    payload: StudentCreate,
    session: Session = Depends(get_session),
):
    """Обновить студента."""
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    student.name = payload.name
    student.group = payload.group
    student.score = payload.score
    session.commit()
    session.refresh(student)
    return student


@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int, session: Session = Depends(get_session)):
    """Удалить студента."""
    student = session.get(Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Студент не найден")
    session.delete(student)
    session.commit()
