from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Status = Status.pending


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Optional[Status] = None
