from fastapi import APIRouter, Depends
from src.services import auth_service
from src.schemas.user import UserCreate, UserResponse, LoginRequest
from sqlalchemy.orm import Session
from config.database import get_db
from src import models
from src.middlewares.auth_middleware import auth_middleware

authRouter = APIRouter(prefix="/auth", tags=["Auth"])


@authRouter.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    data = auth_service.create_user(db, user)
    return {
        "success": True,
        "message": "User registered successfully...",
        "data": UserResponse.model_validate(data),
    }


@authRouter.post("/login")
def login(user: LoginRequest, db: Session = Depends(get_db)):
    token = auth_service.login(db, user)
    return {
        "success": True,
        "message": "User logged-in successfully...",
        "token": token,
    }


@authRouter.get("/me")
def getUser(auth_user: models.User = Depends(auth_middleware)):
    return {
        "success": True,
        "message": "User Fetched successfully",
        "data": UserResponse.model_validate(auth_user),
    }
