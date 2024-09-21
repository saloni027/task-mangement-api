from src.database.models import Tasks
from src.database.config import db_dependency
from src.routes.task_router import task_router
from fastapi import HTTPException, status

@task_router.get(path="/{task_id}",status_code=status.HTTP_200_OK)
def get_task(task_id: int, db: db_dependency):
    task = db.query(Tasks).filter(Tasks.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return task
