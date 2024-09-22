from src.database.schemas import Task, Status
from src.database.config import db_dependency
from src.database.db_operations import get_tasks_from_db
from src.routes.task_router import task_router
from fastapi import status

@task_router.get(path="", status_code=status.HTTP_200_OK)
async def get_task_list(db: db_dependency, status: Status = None):
    tasks = await get_tasks_from_db(db, status)
    return {"tasks":tasks}
















