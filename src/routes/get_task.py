from src.database.config import db_dependency
from src.utils.db_operations import get_task_from_db
from src.routes.task_router import task_router
from fastapi import HTTPException, status


@task_router.get(path="/{task_id}", status_code=status.HTTP_200_OK)
async def get_task(task_id: int, db: db_dependency):
    """
    Retrieve a task from the database by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.
        db: The database session dependency.

    Returns:
        JSON response: The details of the retrieved task.

    Raises:
        HTTPException:
            - 404: If the task with the specified ID does not exist.
    """
    task = await get_task_from_db(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")
    return {"task": task}
