from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    status: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    model_config = {"from_attributes": True}


class Pagination(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int


class UserListResponse(BaseModel):
    success: bool
    message: str
    data: List[UserResponse]
    pagination: Pagination


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    phone: Optional[str] = None


class UpdateUser(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    status: Optional[bool] = None


class LoginRequest(BaseModel):
    email: str
    password: str
