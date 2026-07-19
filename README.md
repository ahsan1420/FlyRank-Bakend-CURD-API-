# Task Management API

A RESTful Task Management API built with FastAPI for the FlyRank Backend Assignment.

## Features

- Create Tasks
- Read All Tasks
- Read Task by ID
- Update Tasks
- Delete Tasks
- Input Validation
- Proper HTTP Status Codes
- Interactive Swagger Documentation

## Technologies Used

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic

## Installation

```bash
git clone https://github.com/ahsan1420/FlyRank-Bakend-CURD-API-.git
cd FlyRank-Bakend-CURD-API-
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn main:app --reload
```

Open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API Information |
| GET | /health | Health Check |
| GET | /tasks | Get All Tasks |
| GET | /tasks/{id} | Get Task by ID |
| POST | /tasks | Create Task |
| PUT | /tasks/{id} | Update Task |
| DELETE | /tasks/{id} | Delete Task |

## Author

Ahsan Sajjad