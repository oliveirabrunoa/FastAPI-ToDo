from fastapi import FastAPI, status
import json
from database import SessionLocal
from typing import List
import models
from pydantic import BaseModel

app = FastAPI()
db = SessionLocal()

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: bool

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    title: str
    description: str
    status: bool

@app.get("/tasks", response_model=List[Task], status_code=status.HTTP_200_OK)
def get_all_taks() -> dict:
    tasks = db.query(models.Task).all()
    return tasks

@app.get("/tasks/{task_id}", response_model=Task, status_code=status.HTTP_200_OK)
def get_an_task(task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    return task

@app.post("/task", response_model=TaskCreate, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task=models.Task(title=task.title,
                         description=task.description,
                         status=task.status)
    db.add(new_task)
    db.commit()
    return new_task

@app.put("/task/{task_id}", response_model=TaskCreate, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: TaskCreate):
    update_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    update_task.title = task.title
    update_task.description = task.description
    update_task.status = task.status
    db.commit()
    return update_task

@app.delete("/task/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int) -> dict:
    item_to_delete = db.query(models.Task).filter(models.Task.id == task_id).first()
    db.delete(item_to_delete)
    db.commit()
    return {"message": "Task deleted successfully"}
