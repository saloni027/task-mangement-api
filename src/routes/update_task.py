from src.database.schemas import TaskUpdate, TaskResponse
from src.database.models import Tasks
from src.database.config import db_dependency
from src.utils.serialize_response import serialize_response
from src.database.db_operations import filter_task_by_id, update_task_to_db
from src.routes.task_router import task_router
from fastapi import status
from src.auth.token_handler import verify_token

# token:verify_token

@task_router.put(path="/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: TaskUpdate, db: db_dependency ):
    db_task = await filter_task_by_id(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
        
    await update_task_to_db(db_task, task,  db)
    updated_task = serialize_response(db_task)

    return updated_task