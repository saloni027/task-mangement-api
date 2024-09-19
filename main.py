from fastapi import FastAPI
from src.database.config import init_db
from src.routes.get_tasks import task_get_router

app = FastAPI()

init_db()
app.include_router(task_get_router)
