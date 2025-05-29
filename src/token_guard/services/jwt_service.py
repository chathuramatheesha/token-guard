from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone, timedelta

import ulid
from jose import jwt, JWTError

from token_guard.enums import TokenType
from token_guard.exceptions import token_exceptions as exceptions
from token_guard.exceptions.common_exceptions import dataclass_invalid_exception
from token_guard.schemas import (
    AccessTokenDTO,
    RefreshTokenDTO,
)
from token_guard.schemas.token_schemas import EmailVerificationTokenDTO


class JWTService:
    def __init__(
        self,
        secret_key: str,
        secret_key_access: str,
        secret_key_refresh: str,
        algorithm: str,
        access_expire: int,
        refresh_expire: int,
        email_verification_expire: int,
    ) -> None:
        self._secret_key = secret_key
        self._secret_key_access = secret_key_access
        self._secret_key_refresh = secret_key_refresh
        self._algorithm = algorithm
        self._access_expire_minutes = access_expire
        self._refresh_expire_days = refresh_expire
        self._email_verification_expire_minutes = email_verification_expire

    def encode_token(self, user_id: str, token_type: TokenType, **extra_fields) -> str:
        expires_at = datetime.now(timezone.utc)

        if token_type == TokenType.ACCESS_TOKEN:
            secret_key = self._secret_key_access
            dto_class = AccessTokenDTO
            expires_at += timedelta(minutes=self._access_expire_minutes)
        elif token_type == TokenType.REFRESH_TOKEN:
            secret_key = self._secret_key_refresh
            dto_class = RefreshTokenDTO
            expires_at += timedelta(days=self._refresh_expire_days)
        elif token_type == TokenType.EMAIL_VERIFICATION_TOKEN:
            secret_key = self._secret_key
            dto_class = EmailVerificationTokenDTO
            expires_at += timedelta(minutes=self._email_verification_expire_minutes)
        else:
            raise exceptions.jwt_token_invalid_type_exception

        if not is_dataclass(dto_class):
            raise dataclass_invalid_exception

        payload = dto_class(
            sub=user_id,
            jti=str(ulid.new()),
            iat=datetime.now(timezone.utc),
            exp=expires_at,
            **extra_fields,
        )

        return jwt.encode(asdict(payload), key=secret_key, algorithm=self._algorithm)

    def decode_token(
        self,
        token: str,
        token_type: TokenType,
    ) -> AccessTokenDTO | RefreshTokenDTO | EmailVerificationTokenDTO:
        try:
            if token_type == TokenType.ACCESS_TOKEN:
                secret_key = self._secret_key_access
                dto_class = AccessTokenDTO
            elif token_type == TokenType.REFRESH_TOKEN:
                secret_key = self._secret_key_refresh
                dto_class = RefreshTokenDTO
            elif token_type == TokenType.EMAIL_VERIFICATION_TOKEN:
                secret_key = self._secret_key
                dto_class = EmailVerificationTokenDTO
            else:
                raise exceptions.jwt_token_invalid_type_exception

            payload = jwt.decode(token, key=secret_key, algorithms=[self._algorithm])

            if not is_dataclass(dto_class):
                raise dataclass_invalid_exception

            token_obj = dto_class(**payload)

            if (
                not token_obj.jti
                or not token_obj.sub
                or not token_obj.exp
                or not token_obj.iat
            ):
                raise exceptions.jwt_token_invalid_exception

            current_datetime = datetime.now(timezone.utc)
            expires_at = payload.get("exp")
            issued_at = payload.get("iat")

            if not expires_at or not issued_at:
                raise exceptions.jwt_token_invalid_exception

            token_obj.exp = datetime.fromtimestamp(expires_at, tz=timezone.utc)
            token_obj.iat = datetime.fromtimestamp(issued_at, tz=timezone.utc)

            if not token_obj.exp or token_obj.exp < current_datetime:
                raise exceptions.jwt_token_expired_exception

            return token_obj

        except JWTError:
            raise exceptions.jwt_credentials_exception
