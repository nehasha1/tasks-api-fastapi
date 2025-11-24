
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: Optional[str]
    email: EmailStr
    created_at: Optional[datetime]

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskOut(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]
    status: str
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
