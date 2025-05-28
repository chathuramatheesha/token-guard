from dataclasses import asdict
from datetime import datetime, timezone, timedelta

import ulid
from jose import jwt, JWTError

from token_guard.exceptions import token_exceptions as exceptions
from token_guard.schemas import (
    AccessTokenDTO,
    RefreshTokenDTO,
)


class JWTService:
    def __init__(
        self,
        secret_key_access: str,
        secret_key_refresh: str,
        algorithm: str,
        access_expire: int,
        refresh_expire: int,
    ) -> None:
        self._secret_key_access = secret_key_access
        self._secret_key_refresh = secret_key_refresh
        self._algorithm = algorithm
        self._access_expire_minutes = access_expire
        self._refresh_expire_days = refresh_expire

    def _encode(self, payload: dict, secret_key: str) -> str:
        return jwt.encode(payload, key=secret_key, algorithm=self._algorithm)

    def _decode(self, token: str, secret_key: str) -> dict:
        try:
            payload = jwt.decode(token, key=secret_key, algorithms=[self._algorithm])
            return payload
        except JWTError:
            raise exceptions.jwt_credentials_exception

    def create_access_token(self, user_id: str) -> str:
        access_token_create = AccessTokenDTO(
            sub=user_id,
            exp=datetime.now(timezone.utc)
            + timedelta(minutes=self._access_expire_minutes),
            iat=datetime.now(timezone.utc),
            jti=str(ulid.new()),
        )
        return self._encode(
            asdict(access_token_create), secret_key=self._secret_key_access
        )

    def create_refresh_token(self, user_id: str, ip_address: str) -> str:
        refresh_token_create = RefreshTokenDTO(
            sub=user_id,
            exp=datetime.now(timezone.utc) + timedelta(days=self._refresh_expire_days),
            jti=str(ulid.new()),
            iat=datetime.now(timezone.utc),
            type="refresh",
            ip=ip_address,
        )
        return self._encode(
            asdict(refresh_token_create), secret_key=self._secret_key_refresh
        )

    def decode_access_token(self, token: str) -> AccessTokenDTO:
        try:
            payload = self._decode(token, secret_key=self._secret_key_access)
            access_token_obj = AccessTokenDTO(**payload)

            current_datetime = datetime.now(timezone.utc)
            expires_at = payload.get("exp")
            issued_at = payload.get("iat")

            if not expires_at.exp or not issued_at:
                raise exceptions.jwt_token_invalid_exception

            access_token_obj.exp = datetime.fromtimestamp(expires_at, tz=timezone.utc)
            access_token_obj.iat = datetime.fromtimestamp(issued_at, tz=timezone.utc)

            if access_token_obj.exp < current_datetime:
                raise exceptions.jwt_token_expired_exception

            if not access_token_obj.jti:
                raise exceptions.jwt_token_invalid_exception

            if not access_token_obj.sub:
                raise exceptions.jwt_credentials_exception

            return access_token_obj
        except JWTError:
            raise exceptions.jwt_credentials_exception

    def decode_refresh_token(self, token: str) -> RefreshTokenDTO:
        try:
            payload = self._decode(token, secret_key=self._secret_key_refresh)
            refresh_token_obj = RefreshTokenDTO(**payload)

            current_datetime = datetime.now(timezone.utc)
            expires_at = payload.get("exp")
            issued_at = payload.get("iat")

            if not expires_at or not issued_at:
                raise exceptions.jwt_token_invalid_exception

            refresh_token_obj.exp = datetime.fromtimestamp(expires_at, tz=timezone.utc)
            refresh_token_obj.iat = datetime.fromtimestamp(issued_at, tz=timezone.utc)

            if refresh_token_obj.exp < current_datetime:
                raise exceptions.jwt_token_expired_exception

            if not refresh_token_obj.jti:
                raise exceptions.jwt_token_invalid_exception

            if not refresh_token_obj.sub:
                raise exceptions.jwt_credentials_exception

            return refresh_token_obj
        except JWTError:
            raise exceptions.jwt_credentials_exception
