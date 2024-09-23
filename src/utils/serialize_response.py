from src.database.schemas import TaskResponse


def serialize_response(new_task):
    """
    Serialize a task object into a TaskResponse model.

    Args:
        new_task: The task object to serialize, which must contain
                   attributes: id, title, description, due_date, and status.

    Returns:
        TaskResponse: A serialized response model containing task details.
    """
    task_response = TaskResponse(
        id=new_task.id,
        title=new_task.title,
        description=new_task.description,
        due_date=new_task.due_date,
        status=new_task.status,
    )
    return task_response
