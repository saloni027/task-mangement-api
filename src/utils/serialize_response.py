from src.database.schemas import TaskResponse

def serialize_response(new_task):
    task_response = TaskResponse(id= new_task.id, title=new_task.title, description=new_task.description, due_date=new_task.due_date, status=new_task.status)
    return task_response