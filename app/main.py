
from fastapi import FastAPI
from app.database import init_db
from app.routes_auth import router as auth_router
from app.routes_tasks import router as tasks_router


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Tasks API. Use /auth/register or /auth/login to test."}

def create_app():
    app = FastAPI(title="Tasks API (JWT Auth)")
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
    return app

app = create_app()

from app.database import Base, engine

@app.on_event("startup")
def on_startup():
    # Automatically create all tables in the database
    Base.metadata.create_all(bind=engine)

# --- auto-added health endpoint for Render ---
from fastapi import FastAPI
try:
    # append health route if not present
    @app.get("/health")
    def health():
        return {"status":"ok"}
except Exception:
    pass
# --- end ---
