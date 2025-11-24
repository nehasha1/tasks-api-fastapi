
from fastapi import FastAPI
from app.database import init_db
from app.routes_auth import router as auth_router
from app.routes_tasks import router as tasks_router

def create_app():
    app = FastAPI(title="Tasks API (JWT Auth)")
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
    return app

app = create_app()

@app.on_event("startup")
def on_startup():
    init_db()
