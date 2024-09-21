from fastapi import FastAPI
from src.database.config import init_db
from src.routes.task_router import task_router
from src.routes import create_task, get_task, get_tasks, delete_task, update_task

app = FastAPI()

init_db()
app.include_router(task_router)


