from src.database.schemas import TaskUpdate, Status
from src.database.config import db_dependency
from src.utils.serialize_response import serialize_response
from src.utils.db_operations import filter_task_by_id, update_task_to_db
from src.routes.task_router import task_router
from fastapi import status, Depends, HTTPException
from src.auth.auth_bearer import JWTBearer


@task_router.put(
    path="/{task_id}",
    dependencies=[Depends(JWTBearer())],
    status_code=status.HTTP_200_OK,
)
async def update_task(task_id: int, task: TaskUpdate, db: db_dependency):
    """
    Update an existing task in the database by its ID.

    Args:
        task_id (int): The ID of the task to update.
        task (TaskUpdate): The new data to update the task with.
        db: The database session dependency.

    Returns:
        JSON response: The updated task details.

    Raises:
        HTTPException:
            - 404: If the task with the specified ID does not exist.
            - 400: If the provided status is invalid.
    """

    db_task = await filter_task_by_id(task_id, db)
    if not db_task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")

    if task.status and task.status not in Status.__members__:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status '{task.status}', valid statuses are {list(Status)}",
        )

    await update_task_to_db(db_task, task, db)
    updated_task = serialize_response(db_task)

    return updated_task
