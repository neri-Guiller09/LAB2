This repository contains a To-Do List API developed using FastAPI. The API allows users to create, retrieve, update, and delete tasks. Each task contains an ID, title, description, and status indicating whether it is finished or not.

Features

Developed using FastAPI.

Implements CRUD operations for managing tasks.

Uses necessary data validation checks (null values, negative numbers, etc.).

Returns appropriate response messages for success and error handling.

Provides Swagger UI for testing API endpoints.

Installation

To set up and run this FastAPI application, follow these steps:

Prerequisites

Python 3.8 or later

pip (Python package installer)

Steps

1. Clone the repository:
``` bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```
2. Create a virtual environment (optional but recommended):
``` bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
3. Install dependencies:
``` bash
pip install -r requirements.txt
```
**Running the Application**

1. Start the FastAPI server:
``` bash
uvicorn main:app --reload
```
2. Open your browser or use a tool like Postman to test the API at:
``` bash
http://127.0.0.1:8000
```
**API Endpoints**
``` bash
GET /tasks/{task_id}
```
Request:

task_id: Integer value representing the task ID.

Response:

If task exists:
``` bash
{
  "task_id": 1,
  "task_title": "Laboratory Activity",
  "task_desc": "Create Lab Act 2",
  "is_finished": false
}
```
If task not found:
``` bash
{
  "error": "Task not found"
}
```
POST /tasks

Request Body:
``` bash
{
  "task_title": "New Task",
  "task_desc": "Task Description",
  "is_finished": false
}
```
Response:
``` bash
{
  "status": "ok",
  "task_id": 2
}
```
PATCH /tasks/{task_id}

Request Body (any updatable field):
``` bash
{
  "is_finished": true
}
```
Response:
``` bash
{
  "status": "ok",
  "updated_task": {
    "task_id": 1,
    "task_title": "Laboratory Activity",
    "task_desc": "Create Lab Act 2",
    "is_finished": true
  }
}
```
DELETE /tasks/{task_id}

Response:
``` bash
{
  "status": "ok",
  "message": "Task deleted successfully"
}
```
Dependencies

This project requires the following dependencies, listed in requirements.txt:

FastAPI

Uvicorn

Testing

You can test the API using the built-in Swagger UI provided by FastAPI:

Open http://127.0.0.1:8000/docs in your browser.

Try the GET, POST, PATCH, and DELETE endpoints.

Required Output

Python file containing the API code.

requirements.txt file listing dependencies.

Screenshot of Swagger UI.

Author

[[Guiller Neri] - Your GitHub Profile](https://github.com/neri-Guiller09)

[Repository Link](https://github.com/neri-Guiller09/LAB2)
