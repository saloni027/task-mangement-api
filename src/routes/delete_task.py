from src.database.config import db_dependency
from src.routes.task_router import task_router
from fastapi import HTTPException, status
from src.database.db_operations import filter_task_by_id, delete_task_from_db
from src.auth.token_handler import verify_token
# token:verify_token
@task_router.delete(path="/{task_id}", status_code=status.HTTP_200_OK)
async def delete_task(task_id: int, db: db_dependency ):
    task = await filter_task_by_id(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")

    await delete_task_from_db(task, db)
   
    return {"detail": "Task deleted"}