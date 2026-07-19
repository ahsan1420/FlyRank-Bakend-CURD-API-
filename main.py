from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Task Management API",
    description="""
A simple REST API built with FastAPI.

## Features
- Create a task
- Read all tasks
- Read a task by ID
- Update a task
- Delete a task

Built for the FlyRank Backend Assignment.
""",
    version="1.0.0",
    contact={
        "name": "Ahsan Sajjad",
        "email": "your-email@example.com"
    }
)


# Request model for creating a task
class TaskCreate(BaseModel):
    title: str


# Request model for updating a task
class TaskUpdate(BaseModel):
    title: str
    done: bool


# In-memory task list
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Build CRUD API",
        "done": False
    },
    {
        "id": 3,
        "title": "Push to GitHub",
        "done": True
    }
]


# Root endpoint
@app.get("/", summary="API Information", tags=["General"])
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": [
            "/tasks"
        ]
    }


# Health endpoint
@app.get("/health", summary="Health Check", tags=["General"])
def health():
    return {
        "status": "ok"
    }


# Get all tasks
@app.get("/tasks", summary="Get all tasks", tags=["Tasks"])
def get_tasks():
    return tasks


# Get single task
@app.get("/tasks/{task_id}", summary="Get task by ID", tags=["Tasks"])
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# Create a new task
@app.post("/tasks", summary="Create a task", tags=["Tasks"], status_code=201)
def create_task(task: TaskCreate):

    if not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


# Update a task
@app.put("/tasks/{task_id}", summary="Update a task", tags=["Tasks"])
def update_task(task_id: int, updated_task: TaskUpdate):

    for task in tasks:

        if task["id"] == task_id:

            if not updated_task.title.strip():
                raise HTTPException(
                    status_code=400,
                    detail="Title cannot be empty"
                )

            task["title"] = updated_task.title
            task["done"] = updated_task.done

            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# Delete a task
@app.delete("/tasks/{task_id}", summary="Delete a task", tags=["Tasks"], status_code=204)
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )
