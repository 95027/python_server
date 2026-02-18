from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from config.database import get_db
from src import models
from src.helpers.auth import decode_access_token


def auth_middleware(request: Request, db: Session = Depends(get_db)):

    authorization = request.headers.get("Authorization")

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")

    token = authorization.split(" ")[1]

    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = db.query(models.User).filter(models.User.id == payload.get("id")).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    request.state.user = user

    return user
