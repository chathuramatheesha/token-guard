from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, ConfigDict

from token_guard.enums import UserRole


class UserCreate(BaseModel):
    id: str
    fullname: str = Field(min_length=5)
    email: str
    hashed_password: str = Field(min_length=8)
    role: UserRole
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    fullname: str
    email: str
    hashed_password: str
    role: UserRole
    created_at: datetime
    updated_at: datetime | None
    last_login_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


# REQUESTS
class UserCreateRequest(BaseModel):
    fullname: str = Field(max_length=255, min_length=5)
    email: EmailStr
    password: str = Field(min_length=8)


class UserUpdateRequest(BaseModel):
    fullname: str | None = None
    email: str | None = None
    hashed_password: str | None = None
    role: UserRole | None = None
    updated_at: datetime | None = None
    last_login_at: datetime | None = None


# RESPONSES
class UserPublicResponse(BaseModel):
    fullname: str
    email: str
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
