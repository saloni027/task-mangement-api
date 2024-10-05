from fastapi import FastAPI
from src.database.config import init_db
from src.routes.task_router import task_router
from src.auth.auth_router import auth_router
from src.routes import create_task, get_task, get_tasks, delete_task, update_task
from src.auth import auth_routes
from typing import AsyncGenerator
from contextlib import asynccontextmanager
from decouple import config

@asynccontextmanager
async def lifespan(
    app: FastAPI,
) -> AsyncGenerator:
    """Application lifespan."""
    if not config("ENVIRONMENT") == "test":
        await init_db()
    yield


app = FastAPI(
    lifespan=lifespan,
)

app.include_router(task_router) 
app.include_router(auth_router)

