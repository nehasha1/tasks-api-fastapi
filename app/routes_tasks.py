
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.auth import get_current_user, get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.TaskOut])
def list_tasks(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.get_tasks_for_user(db, user_id=current_user.id)

@router.post("/", response_model=schemas.TaskOut)
def create_task(task_in: schemas.TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.create_task(db, user_id=current_user.id, title=task_in.title, description=task_in.description)

@router.get("/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = crud.get_task(db, task_id=task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task_in: schemas.TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = crud.get_task(db, task_id=task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db, task=task, title=task_in.title, description=task_in.description)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    task = crud.get_task(db, task_id=task_id)
    if not task or task.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, task=task)
    return {"detail": "deleted"}
