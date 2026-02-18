from sqlalchemy.orm import Session
from src import models
from fastapi import HTTPException, Request


def get_users(db: Session):

    try:
        db_users = db.query(models.User).all()
        return {
            "success": True,
            "message": "Users fetched successfully...",
            "data": db_users,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching users")


def delete_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
