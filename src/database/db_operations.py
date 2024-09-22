
from src.database.models import Tasks

async def get_task_from_db(task_id, db):
    task = await filter_task_by_id(task_id, db)
    return task

async def get_tasks_from_db(db, status):
    all_tasks = db.query(Tasks).all()
    if status:
        tasks = db.query(Tasks).filter(Tasks.status == status).all()
        return tasks
    return all_tasks

async def add_task_to_db(task, db):
    new_task = Tasks(title=task.title, description=task.description, due_date=task.due_date, status=task.status)
    await _save_to_db(new_task, db)
    return new_task

async def filter_task_by_id(task_id, db):
    db_task = db.query(Tasks).filter(Tasks.id==task_id).first()
    return db_task

async def update_task_to_db(db_task, task, db):
    
    db_task.title = task.title or db_task.title
    db_task.description = task.description or  db_task.description
    db_task.due_date = task.due_date or db_task.due_date
    db_task.status = task.status or  db_task.status
    await _commit_to_db(db)
    return 

async def delete_task_from_db(task, db):
    await _delete_from_db(task, db)
    return 

async def _save_to_db(obj, db):
    db.add(obj)
    await _commit_to_db(db)

async def _delete_from_db(obj, db):
    db.delete(obj)
    await _commit_to_db(db)

async def _commit_to_db(db):
    db.commit()





