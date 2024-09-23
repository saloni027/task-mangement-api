from src.database.schemas import Status
from src.database.config import db_dependency
from src.utils.db_operations import get_tasks_from_db
from src.routes.task_router import task_router
from fastapi import status


@task_router.get(path="", status_code=status.HTTP_200_OK)
async def get_task_list(db: db_dependency, status: Status = None):
    """
    Retrieve a list of tasks from the database.

    Args:
        db: The database session dependency.
        status (Status, optional): The status filter for retrieving tasks. 
                                   If not provided, retrieves all tasks.

    Returns:
        JSON response: A list of tasks, potentially filtered by status.
    """
    tasks = await get_tasks_from_db(db, status)
    return {"tasks": tasks}
