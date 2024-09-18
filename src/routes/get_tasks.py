from src.database.schemas import Task
from fastapi import APIRouter

task_get_router = APIRouter(prefix="/tasks")

all_tasks = [
    {"id": 1, "title": "task1", "description": "New task", "status": "pending"},
    {"id": 2, "title": "task2", "description": "New task1", "status": "completed"},
]


@task_get_router.get(path="")
def get_task_list(status: str | None = None):
    if status:
        task_with_status = list(filter(lambda x: x["status"] == status, all_tasks))
        return task_with_status

    return {"all_tasks": all_tasks}


@task_get_router.get(path="/{task_id}")
def get_task(task_id: int):
    task = list(filter(lambda x: x["id"] == task_id, all_tasks))
    return {"task": task}
