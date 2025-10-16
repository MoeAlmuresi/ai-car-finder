from fastapi import FastAPI
from app.db import engine, Base
from app.routers import car
from app import models  # Add this import

# Create tables (dev only; in prod use Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Car Finder API - DB")

app.include_router(car.router)

@app.get("/healthz")
def healthz():
    return {"ok": True}
