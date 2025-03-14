from fastapi import FastAPI, status
import json
from database import SessionLocal
from typing import List
from models import Task

app = FastAPI()
db = SessionLocal()

@app.get("/tasks", status_code=status.HTTP_200_OK)
def get_all_taks() -> dict:
    taks = db.query(Task).all()
    return {'taks': taks}

@app.get("/task/{task_id}")
def task(task_id: int):
    pass

@app.post("/task", status_code=status.HTTP_201_CREATED)
def create_task(task: dict) -> dict:
    pass

@app.put("/task/{task_id}")
def update_task(task_id: int) -> dict:
    pass

@app.delete("/task/{task_id}")
def delete_task(task_id: int) -> dict:
    pass
