from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.database.database import engine
from app.database.models.user import SQLModel

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/")
def root():
    return {"message": "API funcionando"}