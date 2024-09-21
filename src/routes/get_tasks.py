from src.database.schemas import Task
from src.database.models import Tasks
from src.database.config import db_dependency
from src.routes.task_router import task_router

@task_router.get(path="")
def get_task_list(db: db_dependency, status: str | None = None):
    all_tasks = db.query(Tasks).all()
    if status:
        task = db.query(Tasks).filter(Tasks.status == status).all()
        return {"task": task}

    return {"all_tasks":all_tasks}
















