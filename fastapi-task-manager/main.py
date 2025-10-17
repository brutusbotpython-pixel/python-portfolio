"""Task Manager API"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Task Manager API", version="1.0.0")

tasks = {}
counter = 0

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "medium"

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    created_at: datetime

@app.get("/")
async def root():
    return {"message": "Task Manager API", "docs": "/docs"}

@app.post("/api/v1/tasks", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    global counter
    counter += 1
    new_task = {
        "id": counter,
        "title": task.title,
        "description": task.description,
        "status": "todo",
        "priority": task.priority,
        "created_at": datetime.utcnow()
    }
    tasks[counter] = new_task
    return TaskResponse(**new_task)

@app.get("/api/v1/tasks", response_model=List[TaskResponse])
async def get_tasks():
    return [TaskResponse(**t) for t in tasks.values()]

@app.get("/api/v1/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Not found")
    return TaskResponse(**tasks[task_id])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
