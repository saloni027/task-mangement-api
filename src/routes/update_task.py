from src.database.schemas import TaskUpdate, TaskResponse
from src.database.models import Tasks
from src.database.config import db_dependency
from src.routes.task_router import task_router
from fastapi import status
from src.auth.token_handler import verify_token

@task_router.put(path="/{task_id}", response_model=TaskResponse, status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: TaskUpdate, db: db_dependency, token:verify_token ):
    db_task = db.query(Tasks).filter(Tasks.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")

    db_task.title = task.title or db_task.title
    db_task.description = task.description or  db_task.description
    db_task.due_date = task.due_date or db_task.due_date
    db_task.status = task.status or  db_task.status

    db.commit()

    updated_task = TaskResponse(id= db_task.id, title=db_task.title, description=db_task.description, due_date=db_task.due_date, status=db_task.status)
    
    return db_task