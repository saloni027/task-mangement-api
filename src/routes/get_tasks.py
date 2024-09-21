from src.database.schemas import Task
from src.database.models import Tasks
from src.database.config import db_dependency
from src.routes.task_router import task_router

@task_router.get(path="")
def get_task_list(db: db_dependency, status: str | None = None):
    all_tasks = db.query(Tasks).all()

    if status:
        task_with_status = list(filter(lambda x: x["status"] == status, all_tasks))
        return {"task_with_status": task_with_status}

    return {"all_tasks":all_tasks}















# from fastapi import APIRouter
# task_get_router = APIRouter(prefix="/tasks")

# @task_get_router.get(path="")
# def get_task_list(status: str | None = None, db: db_dependency):
#     if status:
#         task_with_status = list(filter(lambda x: x["status"] == status, all_tasks))
#         return task_with_status

#     all_tasks = db.query(Tasks).all()
#     return all_tasks


# @task_get_router.get(path="/{task_id}")
# def get_task(task_id: int, db: db_dependency):
#     task_by_id = db.query(Tasks).filter(Tasks.id==task_id).first()
#     return task_by_id

