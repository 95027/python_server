# User Management Mini Application

## Overview

This is a full-stack user management application with authentication and CRUD operations built with FastAPI and Python.

## Features

- JWT-based authentication

- Register and Login endpoints

- Get all users with formatted JSON response

- Delete user (self-delete prevention)

- Global authentication middleware

- Service layer for business logic separation

- Pydantic schemas for request validation and response formatting

- Input validation for user data (email, password, phone, etc.)

- Consistent error handling with proper HTTP status codes

## Tech Stack

- Backend: Python, FastAPI
- Database: SQLite
- Frontend: React

## Setup Instructions

### Backend

1. Clone the repo

   ```bash
   git clone <REPO_URL>
   cd python_server

   ```

2. Create virtual environment

   ```bash
   python -m venv venv
   venv\Scripts\activate # Windows
   source venv/bin/activate # Linux/macOS
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Create .env with:

   ```bash
   DATABASE_URL=sqlite:///./database.db
   SECRET_KEY=your_super_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=60
   ```

5. Run server
   ```bash
   uvicorn main:app --reload
   ```

6. Access API documentation (Swagger UI):
    ```bash
    http://localhost:8000/docs
    ```
