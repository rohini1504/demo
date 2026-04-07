from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, services
from .database import get_db

router = APIRouter()

@router.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return services.create_task(db, task)

@router.get("/tasks", response_model=list[schemas.TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return services.get_tasks(db)

@router.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, status: str, db: Session = Depends(get_db)):
    updated = services.update_task_status(db, task_id, status)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated
