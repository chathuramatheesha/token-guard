from dataclasses import dataclass
from datetime import datetime

from token_guard.enums import TokenType


@dataclass
class TokenBase:
    sub: str
    jti: str
    exp: datetime
    iat: datetime


# ACCESS TOKEN
@dataclass
class AccessTokenDTO(TokenBase):
    pass


# REFRESH TOKEN
@dataclass
class RefreshTokenDTO(TokenBase):
    type: TokenType
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


# EMAIL VERIFICATION TOKEN
@dataclass
class EmailVerificationTokenDTO(TokenBase):
    type: TokenType


@dataclass
class EmailSendDTO:
    subject: str
    email_from: str
    email_to: str
    content: str
