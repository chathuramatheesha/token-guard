from dataclasses import dataclass

from pydantic import BaseModel, EmailStr


# DTOs
@dataclass
class AuthTokens:
    access_token: str
    refresh_token: str
    token_type: str


# REQUESTS
class AuthLoginRequest(BaseModel):
    email: EmailStr
    password: str


# RESPONSES
class AuthLoginResponse(BaseModel):
    access_token: str
    token_type: str
