
# Tasks API — FastAPI Backend

Minimal backend implementing:
- User registration & login (JWT)
- Task CRUD for authenticated users
- SQLAlchemy ORM (SQLite by default)
- Swagger docs at `/docs`

## Quick start (local)
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. export DATABASE_URL="sqlite:///./test.db"
   export SECRET_KEY="change-this-secret"
   export ACCESS_TOKEN_EXPIRE_MINUTES=60
5. uvicorn app.main:app --reload

API Endpoints:
- POST /auth/register
- POST /auth/login
- GET /tasks
- POST /tasks
- GET /tasks/{id}
- PUT /tasks/{id}
- DELETE /tasks/{id}

Resume bullet (copy-paste):
Built a Task Management REST API using FastAPI with JWT authentication, SQLAlchemy ORM, and Swagger documentation. Code: (GitHub link)
