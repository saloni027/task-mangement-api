from src.database.schemas import Task, TaskResponse
from src.database.models import Tasks
from src.database.config import db_dependency
from src.routes.task_router import task_router

@task_router.post(path="", response_model=TaskResponse)
def create_task(task: Task, db: db_dependency):
    new_task = Tasks(title=task.title, description=task.description, due_date=task.due_date, status=task.status)
    db.add(new_task)
    db.commit()
    task_response = TaskResponse(id= new_task.id, title=new_task.title, description=new_task.description, due_date=task.due_date, status=task.status)
    return task_response
