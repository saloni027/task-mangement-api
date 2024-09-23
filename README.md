# Task Management API

A simple Task Management API to allow users to create, read, update, and delete tasks. It is designed to help you manage your tasks effectively.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Run](#setup-and-run)
- [API Refrence](#api-reference)

## Features
- Create a new task
- Retrieve all tasks
- Retrieve a task by id
- Update a specific task
- Delete a task

## Technologies Used
- Python 3.x
- FastAPI
- Pydantic
- SQLAlchemy

## Setup and Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/task-management-api.git

2. **change directory into repository**:
   ```bash
   cd task-management-api
   
3. **Include enviroment variables**:
   ```bash
   Include a .env file containing SECRET_KEY and DB_URI

4. **Run the application with docker**:
   ```bash
   docker compose --build
   docker compose up

Note: Please use the mocked user1, password1 as username and password for PUT /tasks/<task_id> and DELETE /tasks/<task_id> since the application currently does not support creating users.

## API Reference

#### Get all tasks

```http
  GET /tasks
```
Get the all tasks.

```http
  GET /tasks?status=<task_status>
```
Filter the tasks result with status.
status can be "pending", "completed", "in-progress"

#### Get a task

```http
  GET /tasks/<task_id>
```
Get the task with specified task_id.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of the task  |


#### Create a task

```http
  POST /tasks
```
Create the task.

Add the task data to database.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title` | `str` | **Required**. Title of the task. |
| `description`  | `str` | Description for the task. |
| `due_date`     | `datetime` | Due date for the completion of the task.|
| `status`| `enum` | **Required** Current status of the task with choices pending, completed and in-progress and default sets to pending. |


#### Update a task

```http
  PUT /tasks/<task_id> 
```

Updates the task data to database with the given id.

This endpoint Requires authentication.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of the task  |


This endpoint requires authentication token. To generate the token, Create a POST request with username and password (user1, password1 in this case.) to /auth/token. This will return the token. Include the token in  Authorization headers while sending the request.

if sending the request using FastAPI Swagger, Include the token in the Authorize section at top right.

#### Delete a task

```http
  DELETE /tasks/<task_id> 
```
Deletes the task from database with the given id.

This endpoint Requires authentication.

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of the task  |

This endpoint requires authentication token. To generate the token, Create a POST request with username and password (user1, password1 in this case.) to /auth/token. This will return the token. Include the token in  Authorization headers while sending the request.

if sending the request using FastAPI Swagger, Include the token in the Authorize section at top right.

## Usage/Examples

```

Get /tasks

Response:

{
  "tasks": [
    {
      "due_date": "2024-09-22T08:24:43.883000",
      "title": "task1",
      "id": 6,
      "status": "pending",
      "description": "string"
    },
    {
      "due_date": "2024-09-22T17:27:32.307000",
      "title": "task2",
      "id": 10,
      "status": "pending",
      "description": "string"
    },
    {
      "due_date": "2024-09-23T08:20:04.801000",
      "title": "task3",
      "id": 11,
      "status": "completed",
      "description": "string"
    }
    
  ]
}
```

```
Get /tasks?status=pending

Response:

{
  "tasks": [
    {
      "due_date": "2024-09-22T08:24:43.883000",
      "title": "task1",
      "id": 6,
      "status": "pending",
      "description": "string"
    },
    {
      "due_date": "2024-09-22T17:27:32.307000",
      "title": "task2",
      "id": 10,
      "status": "pending",
      "description": "string"
    }
    
  ]
}

```

```
Get /tasks/1

Response:

{
  "task": {
    "due_date": "2024-09-23T09:05:54.008000",
    "title": "string",
    "id": 1,
    "status": "pending",
    "description": "string"
  }
}


```

```
POST /tasks

Request body:

   {
    "title": "task1",
    "description": "task",
    "due_date": "2024-09-23T12:27:42.853Z",
    "status": "pending"
}

Response:

  {
  "title": "string",
  "description": "string",
  "due_date": "2024-09-23T12:28:16.756000",
  "status": "pending",
  "id": 1
}

```

```

PUT /tasks/1

Request body:

   {
    "title": "task2",
  
  }

Response:

  {
  "title": "task2",
  "description": "string",
  "due_date": "2024-09-23T12:28:16.756000",
  "status": "pending",
  "id": 1
}

```

```
DELETE /tasks/1

Response:

  {
  "detail": "Task deleted"
}

```
