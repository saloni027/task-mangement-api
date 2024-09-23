from sqlalchemy import Column, Integer, String, DateTime, Enum
from src.database.schemas import Status
from src.database.config import Base


class Tasks(Base):
    """
    Represents a task in the database.

    Attributes:
        id (int): The unique identifier for the task.
        title (str): The title of the task.
        description (str, optional): A brief description of the task.
        due_date (DateTime, optional): The date and time by which the task should be completed.
        status (Enum): The current status of the task, defaults to 'pending'.
    """
    __tablename__ = "tasks"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String)
    description: str = Column(String, nullable=True)
    due_date: DateTime = Column(DateTime, nullable=True)
    status: Enum = Column(Enum(Status), default=Status.pending)
