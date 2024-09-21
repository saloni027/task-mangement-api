import enum
import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, Enum
from src.database.config import Base


class Status(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    COMPLETED = "completed"

class Tasks(Base):
    __tablename__ = 'tasks'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String, index=True)
    description: str = Column(String, nullable=True)
    due_date: DateTime = Column(DateTime, nullable=True)
    # type_annotation_map = {
    #     Status: sqlalchemy.Enum(Status, length=50, native_enum=False,default=Status.PENDING)
    # }
    status: Enum = Column(Enum(Status), default=Status.PENDING)


 