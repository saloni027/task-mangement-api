from src.database.schemas import Task, Status
from src.database.models import Tasks
from src.database.config import db_dependency
from src.routes.task_router import task_router
from fastapi import status

@task_router.get(path="", status_code=status.HTTP_200_OK)
def get_task_list(db: db_dependency, status: Status = None):
    all_tasks = db.query(Tasks).all()
    if status:
        tasks = db.query(Tasks).filter(Tasks.status == status).all()
        return {"tasks": tasks}

    return {"all_tasks":all_tasks}
















