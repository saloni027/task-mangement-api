from sqlalchemy import Column, Integer, String, DateTime, Enum
from src.database.schemas import Status
from src.database.config import Base

class Tasks(Base):
    __tablename__ = 'tasks'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String)
    description: str = Column(String, nullable=True)
    due_date: DateTime = Column(DateTime, nullable=True)
    status: Enum = Column(Enum(Status), default=Status.pending)


 