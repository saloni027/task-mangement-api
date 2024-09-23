from src.database.config import db_dependency
from src.routes.task_router import task_router
from fastapi import HTTPException, status, Depends
from src.utils.db_operations import filter_task_by_id, delete_task_from_db
from src.auth.auth_bearer import JWTBearer


@task_router.delete(
    path="/{task_id}",
    dependencies=[Depends(JWTBearer())],
    status_code=status.HTTP_200_OK,
)
async def delete_task(task_id: int, db: db_dependency):
    """
    Delete a task from the database by its ID.

    Args:
        task_id (int): The ID of the task to delete.
        db: The database session dependency.

    Returns:
        JSON response: A confirmation message indicating the task has been deleted.

    Raises:
        HTTPException: 
            - 404: If the task with the specified ID does not exist.
    """
    task = await filter_task_by_id(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")

    await delete_task_from_db(task, db)

    return {"detail": "Task deleted"}
