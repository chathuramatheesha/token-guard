from pydantic import BaseModel


class AuthLoginResponse(BaseModel):
    access_token: str
    token_type: str
