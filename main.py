from fastapi import FastAPI
from config.database import Base, engine
import src.models
from src.routes import router as app_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(app_routes)


@app.get("/")
def read_root():
    return {"message": "FastApi server is running"}
