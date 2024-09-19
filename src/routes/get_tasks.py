from src.database.schemas import Task
from src.database.config import db_dependency
from fastapi import APIRouter
from src.database.models import Tasks

task_get_router = APIRouter(prefix="/tasks")

@task_get_router.get(path="")
def get_task_list(db: db_dependency):
    all_tasks = db.query(Tasks).all()
    return {"all_tasks": all_tasks}
