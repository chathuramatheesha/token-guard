from datetime import datetime

from pydantic import BaseModel, Field, EmailStr

from token_guard.enums import UserRole


class UserCreate(BaseModel):
    nickname: str | None = None
    fullname: str = Field(min_length=5)
    email: str
    hashed_password: str = Field(min_length=8)
    role: UserRole
    created_at: datetime


class UserCreateRequest(BaseModel):
    fullname: str = Field(max_length=255, min_length=5)
    nickname: str | None = None
    email: EmailStr
    password: str = Field(min_length=8)


class UserUpdate(BaseModel):
    fullname: str | None = Field(max_length=255, min_length=5)
    nickname: str | None
