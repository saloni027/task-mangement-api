import enum
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime
from src.database.config import Base

class Status(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"

class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    type_annotation_map = {
        Status: sqlalchemy.Enum(Status, length=50, native_enum=False,default=Status.PENDING)
    }


 