from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]


class Task(BaseModel):
    task_title: str = Field(..., min_length=1, description="Title of the task")
    task_desc: Optional[str] = Field(None, description="Description of the task")
    is_finished: bool = False

class TaskUpdate(BaseModel):
    task_title: Optional[str] = Field(None, min_length=1, description="Title of the task")
    task_desc: Optional[str] = Field(None, description="Description of the task")
    is_finished: Optional[bool] = None

def find_task_by_id(task_id: int):
    for task in task_db:
        if task["task_id"] == task_id:
            return task
    return None

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id <= 0:
        raise HTTPException(status_code=400, detail={"error": "Task ID must be integer, a positive integer"})
    
    task = find_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail={"error": f"Task with id {task_id} not found"})
    
    return {"status": "ok", "STATUS RESULT": task}

@app.post("/tasks")
def create_task(task: Task):
    new_task_id = len(task_db) + 1
    new_task = {
        "task_id": new_task_id,
        "task_title": task.task_title,
        "task_desc": task.task_desc,
        "is_finished": task.is_finished
    }
    task_db.append(new_task)
    
    return {"status": "ok", "ADDED SUCCESSFULLY": new_task}

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    if task_id <= 0:
        raise HTTPException(status_code=400, detail={"error": "Task ID must be integer, positive integer"})
    
    task = find_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail={"error": f"Task with id {task_id} not found"})
    
    if task_update.task_title is not None:
        task["task_title"] = task_update.task_title
    if task_update.task_desc is not None:
        task["task_desc"] = task_update.task_desc
    if task_update.is_finished is not None:
        task["is_finished"] = task_update.is_finished
    
    return {"status": "ok", "UPDATED SUCCESSFULLY": task}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id <= 0:
        raise HTTPException(status_code=400, detail={"error": "Task ID must be integer, positive integer"})
    
    task = find_task_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail={"error": f"Task with id {task_id} not found"})
    
    task_db.remove(task)
    return {"status": "ok", "DELETE SUCCESSFULLY": f"Task with id {task_id} deleted"} 

@app.put("/tasks/{task_id}")
def replace_task(task_id: int, task: Task):
    if task_id <= 0:
        raise HTTPException(status_code=400, detail={"error": "Task ID must be a positive integer"})

    existing_task = find_task_by_id(task_id)
    if existing_task is None:
        raise HTTPException(status_code=404, detail={"error": f"Task with id {task_id} not found"})
    
    existing_task["task_title"] = task.task_title
    existing_task["task_desc"] = task.task_desc
    existing_task["is_finished"] = task.is_finished
    
    return {"status": "ok", "UPDATED SUCCESSFULLY": existing_task}