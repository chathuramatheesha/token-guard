from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, ConfigDict

from token_guard.enums import UserRole


class UserCreate(BaseModel):
    id: str
    nickname: str | None = None
    fullname: str = Field(min_length=5)
    email: str
    hashed_password: str = Field(min_length=8)
    role: UserRole
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    fullname: str | None = Field(max_length=255, min_length=5)
    nickname: str | None


class UserCreateRequest(BaseModel):
    fullname: str = Field(max_length=255, min_length=5)
    nickname: str | None = None
    email: EmailStr
    password: str = Field(min_length=8)


class UserPublicResponse(BaseModel):
    fullname: str
    nickname: str | None
    email: str
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
