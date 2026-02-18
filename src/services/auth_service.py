from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schemas.user import UserCreate, LoginRequest
from src import models
from src.helpers.auth import hash_password, verify_password, create_access_token
from sqlalchemy.exc import SQLAlchemyError


def create_user(db: Session, data: UserCreate):
    try:
        user = db.query(models.User).filter(models.User.email == data.email).first()

        if user:
            raise HTTPException(status_code=400, detail="Email already registered")

        new_user = models.User(
            name=data.name,
            email=data.email,
            password=hash_password(data.password),
            phone=data.phone,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating user")


def login(db: Session, data: LoginRequest):
    try:
        user = db.query(models.User).filter(models.User.email == data.email).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        is_valid = verify_password(data.password, user.password)

        if not is_valid:
            raise HTTPException(status_code=401, detail="Invalid Credentials")

        token = create_access_token({"id": user.id})
        return token
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail="Error Login with user")
