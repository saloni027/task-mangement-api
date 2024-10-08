from src.database.schemas import Task
from src.database.config import db_dependency
from src.utils.db_operations import add_task_to_db
from src.utils.serialize_response import serialize_response
from src.routes.task_router import task_router
from fastapi import status


@task_router.post(path="", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task, db: db_dependency):
    """
    Create a new task in the database.

    Args:
        task (Task): The task object containing the details of the task to create.
        db: The database session dependency.

    Returns:
        JSON response: The created task details, serialized for the response.

    """
    new_task = await add_task_to_db(task, db)
    task_response = serialize_response(new_task)
    return task_response
