from dataclasses import dataclass
from datetime import datetime


# ACCESS TOKEN
@dataclass
class AccessTokenDTO:
    sub: str
    exp: datetime
    iat: datetime
    jti: str


# REFRESH TOKEN
@dataclass
class RefreshTokenDTO:
    sub: str
    exp: datetime
    iat: datetime
    jti: str
    type: str
    ip: str


@dataclass
class RefreshTokenSave:
    jti: str
    user_id: str
    hashed_token: str
    ip_address: str
    device_info: str
    created_at: datetime
    expires_at: datetime
