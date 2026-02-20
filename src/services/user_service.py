from sqlalchemy.orm import Session
from sqlalchemy import or_, desc
from src import models
from fastapi import HTTPException
from src.schemas.user import UpdateUser


def get_users(
    db: Session, page: int, limit: int, search: str | None, status: bool | None
):

    try:
        query = db.query(models.User)

        if search:
            query = query.filter(
                or_(
                    models.User.name.ilike(f"%{search}%"),
                    models.User.email.ilike(f"%{search}%"),
                )
            )

        if status is not None:
            query = query.filter(models.User.status == status)

        query = query.order_by(desc(models.User.created_at))

        total = query.count()

        users = query.offset((page - 1) * limit).limit(limit).all()

        return {
            "success": True,
            "message": "Users fetched successfully...",
            "data": users,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "total_pages": (total + limit - 1) // limit,
            },
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching users")


def update_user(id: int, payload: UpdateUser, db: Session):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        return None

    update_data = payload.dict(exclude_unset=True)

    for key, val in update_data.items():
        setattr(user, key, val)

    db.commit()
    db.refresh(user)
    return user


def delete_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
