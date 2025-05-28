from datetime import datetime, timezone

from fastapi.requests import Request

from token_guard.core import Argon2Hasher
from token_guard.exceptions import auth_exceptions as exceptions
from token_guard.schemas import (
    UserPublicResponse,
    AuthLoginRequest,
    UserCreateRequest,
    AuthTokens,
    UserUpdateRequest,
    RefreshTokenSave,
)
from token_guard.services.jwt_service import JWTService
from token_guard.services.refresh_token_service import RefreshTokenService
from token_guard.services.user_service import UserService


class AuthService:
    def __init__(
        self,
        user_service: UserService,
        jwt_service: JWTService,
        refresh_token_service: RefreshTokenService,
        hasher: Argon2Hasher,
    ) -> None:
        self._user_service = user_service
        self._jwt_service = jwt_service
        self._refresh_token_service = refresh_token_service
        self._hasher = hasher

    async def register_user(
        self, user_create_request: UserCreateRequest
    ) -> UserPublicResponse:
        return await self._user_service.create_user(user_create_request)

    async def update_last_login(self, user_id: str) -> None:
        await self._user_service.update_user(
            user_id=user_id,
            update_user_request=UserUpdateRequest(
                last_login_at=datetime.now(timezone.utc)
            ),
        )
        return

    async def login(
        self, request: Request, user_login_request: AuthLoginRequest
    ) -> AuthTokens:
        user = await self._user_service.get_user_by_email(str(user_login_request.email))

        if not user or not self._hasher.verify_password(
            user_login_request.password, user.hashed_password
        ):
            raise exceptions.auth_invalid_credentials_exception

        user_ip_address = request.client.host
        access_token = self._jwt_service.create_access_token(user.id)
        refresh_token = self._jwt_service.create_refresh_token(user.id, user_ip_address)
        refresh_token_data = self._jwt_service.decode_refresh_token(refresh_token)

        await self._refresh_token_service.save_refresh_token(
            RefreshTokenSave(
                jti=refresh_token_data.jti,
                user_id=refresh_token_data.sub,
                hashed_token=refresh_token,
                created_at=refresh_token_data.iat,
                expires_at=refresh_token_data.exp,
                ip_address=user_ip_address,
                device_info=request.headers.get("user-agent"),
            )
        )
        await self.update_last_login(user.id)

        auth_tokens = AuthTokens(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
        )
        return auth_tokens
