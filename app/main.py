# main.py

from fastapi import FastAPI
from app.database import Base, engine
from app.routes_auth import router as auth_router
from app.routes_tasks import router as tasks_router

def create_app() -> FastAPI:
    app = FastAPI(title="Tasks API (JWT Auth)")

    # --- Root endpoint ---
    @app.get("/")
    def root():
        return {"message": "Welcome to Tasks API. Use /auth/register or /auth/login to test."}

    # --- Health endpoint for Render ---
    @app.get("/health")
    def health():
        return {"status": "ok"}

    # --- Include routers ---
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])

    # --- DB startup ---
    @app.on_event("startup")
    def on_startup():
        Base.metadata.create_all(bind=engine)

    return app

# Create the FastAPI app
app = create_app()
