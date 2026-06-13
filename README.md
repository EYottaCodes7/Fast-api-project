# FastAPI CRUD Application

A simple CRUD (Create, Read, Update, Delete) REST API built with FastAPI. This project demonstrates how to build modern backend services using FastAPI, Pydantic, and a database backend.

## Features

- Create new records
- Read single and multiple records
- Update existing records
- Delete records
- Automatic API documentation
- Request validation using Pydantic
- Fast and asynchronous API endpoints

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- SQLAlchemy
- SQLite (can be replaced with PostgreSQL/MySQL)

## Project Structure

```
project/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── crud.py
│
├── requirements.txt
└── README.md
```

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/fastapi-crud-app.git
cd fastapi-crud-app
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

## Example Endpoints

### Create Item

```http
POST /items
```

### Get All Items

```http
GET /items
```

### Get Item by ID

```http
GET /items/{id}
```

### Update Item

```http
PUT /items/{id}
```

### Delete Item

```http
DELETE /items/{id}
```

## Example Request

```json
{
    "title": "Learn FastAPI",
    "description": "Build CRUD APIs with FastAPI"
}
```

## Learning Objectives

This project was built to practice:

- REST API development
- CRUD operations
- FastAPI fundamentals
- Data validation
- Database integration
- Backend project structure

## Future Improvements

- JWT Authentication
- User management
- PostgreSQL support
- Docker containerization
- Automated testing
- CI/CD pipeline

## License

This project is licensed under the MIT License.

## Author

Eyuel Mekonnen

GitHub: https://github.com/yourusername
