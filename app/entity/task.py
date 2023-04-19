from pydantic import BaseModel
from pydantic.types import Optional
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .base import Base


class Task(Base, BaseModel):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now())


class TaskModel(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None
    created_at: Optional[datetime] = None
