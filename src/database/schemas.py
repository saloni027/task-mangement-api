from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    """
    Enum representing the possible statuses of a task.

    Attributes:
        pending: The task is pending.
        in_progress: The task is currently being worked on.
        completed: The task has been completed.
    """
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"


class Task(BaseModel):
    """
    Schema for creating a new task.

    Attributes:
        title (str): The title of the task.
        description (Optional[str]): A brief description of the task (optional).
        due_date (Optional[datetime]): The date and time by which the task should be completed (optional).
        status (Status): The current status of the task, defaults to 'pending'.
    """
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Status = Status.pending


class TaskUpdate(BaseModel):
    """
    Schema for updating an existing task.

    Attributes:
        title (Optional[str]): The new title of the task (optional).
        description (Optional[str]): The new description of the task (optional).
        due_date (Optional[datetime]): The new due date for the task (optional).
        status (Optional[str]): The new status of the task (optional).
    """
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: Optional[str] = None

class TaskResponse(Task):
    """
    Schema for returning task details in the response.

    Inherits from `Task` and adds an ID attribute.

    Attributes:
        id (int): The unique identifier for the task.
    """
    id: int
    

