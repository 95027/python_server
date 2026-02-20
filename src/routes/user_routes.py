from fastapi import Depends, APIRouter, Request, HTTPException, Query
from sqlalchemy.orm import Session
from config.database import get_db
from src.services import user_service
from src.schemas.user import UserListResponse, UpdateUser, UserResponse

userRouter = APIRouter(prefix="/users", tags=["Users"])


@userRouter.get("", response_model=UserListResponse)
def read_user(
    page: int = Query(1, ge=1),
    limit: int = Query(2, le=100),
    search: str | None = None,
    status: bool | None = None,
    db: Session = Depends(get_db),
):
    return user_service.get_users(db, page, limit, search, status)


@userRouter.put("/{id}")
def update_user(id: int, payload: UpdateUser, db: Session = Depends(get_db)):

    updated = user_service.update_user(id, payload, db)

    if not updated:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "success": True,
        "message": "User updated successfully",
        "data": UserResponse.model_validate(updated),
    }


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
