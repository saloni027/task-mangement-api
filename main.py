from fastapi import FastAPI

from src.routes.get_tasks import task_get_router

app = FastAPI()


app.include_router(task_get_router)
