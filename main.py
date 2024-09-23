from fastapi import FastAPI
from src.database.config import init_db
from src.routes.task_router import task_router
from src.auth.auth_router import auth_router
from src.routes import create_task, get_task, get_tasks, delete_task, update_task
from src.auth import auth_routes

app = FastAPI()

init_db()  # Initialize the database
app.include_router(task_router) # Include task-related routes
app.include_router(auth_router) # Include authentication-related routes
