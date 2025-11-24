
from sqlalchemy.orm import Session
from app import models
from typing import List, Optional

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, name: str, email: str, password_hash: str) -> models.User:
    user = models.User(name=name, email=email, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_task(db: Session, user_id: int, title: str, description: str) -> models.Task:
    task = models.Task(user_id=user_id, title=title, description=description, status="todo")
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks_for_user(db: Session, user_id: int) -> List[models.Task]:
    return db.query(models.Task).filter(models.Task.user_id == user_id).all()

def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(db: Session, task: models.Task, title: str=None, description: str=None, status: str=None):
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if status is not None:
        task.status = status
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task: models.Task):
    db.delete(task)
    db.commit()
    return
