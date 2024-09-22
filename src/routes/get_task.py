from src.database.config import db_dependency
from src.database.db_operations import get_task_from_db
from src.routes.task_router import task_router
from fastapi import HTTPException, status

@task_router.get(path="/{task_id}",status_code=status.HTTP_200_OK)
async def get_task(task_id: int, db:db_dependency):
    task = await get_task_from_db(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return {"task":task}
