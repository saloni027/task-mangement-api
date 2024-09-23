from src.database.models import Tasks


async def get_task_from_db(task_id, db):
    """
    Retrieve a task from the database by its ID.

    Args:
        task_id (int): The ID of the task to retrieve.
        db: The database session.

    Returns:
        Tasks: The task object if found, otherwise None.
    """
    task = await filter_task_by_id(task_id, db)
    return task


async def get_tasks_from_db(db, status):
    """
    Retrieve all tasks from the database, optionally filtered by status.

    Args:
        db: The database session.
        status (str, optional): The status to filter tasks by.

    Returns:
        list: A list of task objects.
    """
    all_tasks = db.query(Tasks).all()
    if status:
        tasks = db.query(Tasks).filter(Tasks.status == status).all()
        return tasks
    return all_tasks


async def add_task_to_db(task, db):
    """
    Add a new task to the database.

    Args:
        task: The task object containing the details to be added.
        db: The database session.

    Returns:
        Tasks: The newly created task object.
    """
    new_task = Tasks(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status=task.status,
    )
    await _save_to_db(new_task, db)
    return new_task


async def filter_task_by_id(task_id, db):
    """
    Filter a task from the database by its ID.

    Args:
        task_id (int): The ID of the task to filter.
        db: The database session.

    Returns:
        Tasks: The task object if found, otherwise None.
    """
    db_task = db.query(Tasks).filter(Tasks.id == task_id).first()
    return db_task


async def update_task_to_db(db_task, task, db):
    """
    Update an existing task in the database.

    Args:
        db_task (Tasks): The task object to update.
        task: The new task details to update.
        db: The database session.

    Returns:
        None
    """

    db_task.title = task.title or db_task.title
    db_task.description = task.description or db_task.description
    db_task.due_date = task.due_date or db_task.due_date
    db_task.status = task.status or db_task.status
    await _commit_to_db(db)
    return


async def delete_task_from_db(task, db):
    """
    Delete a task from the database.

    Args:
        task (Tasks): The task object to delete.
        db: The database session.

    Returns:
        None
    """
    await _delete_from_db(task, db)
    return


async def _save_to_db(obj, db):
    """
    Save an object to the database and commit the transaction.

    Args:
        obj: The object to save.
        db: The database session.

    Returns:
        None
    """
    db.add(obj)
    await _commit_to_db(db)


async def _delete_from_db(obj, db):
    """
    Delete an object from the database and commit the transaction.

    Args:
        obj: The object to delete.
        db: The database session.

    Returns:
        None
    """
    db.delete(obj)
    await _commit_to_db(db)


async def _commit_to_db(db):
    """
    Commit the current transaction to the database.

    Args:
        db: The database session.

    Returns:
        None
    """
    db.commit()
