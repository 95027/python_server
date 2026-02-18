from fastapi import Depends, APIRouter, Request, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from src.services import user_service
from src.schemas.user import UserListResponse
from typing import List

userRouter = APIRouter(prefix="/users", tags=["Users"])


@userRouter.get("", response_model=UserListResponse)
def read_user(db: Session = Depends(get_db)):
    return user_service.get_users(db)


@userRouter.delete("/{id}")
def delete_user(id: int, request: Request, db: Session = Depends(get_db)):
    auth_user = request.state.user

    if auth_user.id == id:
        raise HTTPException(status_code=400, detail="Cannot delete yourself")

    deleted = user_service.delete_user(id, db)

    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "success": True,
        "message": "User deleted successfully",
    }
