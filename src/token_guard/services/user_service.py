from datetime import datetime, timezone

import ulid

from token_guard.core import Argon2Hasher
from token_guard.enums import UserRole
from token_guard.exceptions import user_exceptions as exception
from token_guard.repositories import UserRepository
from token_guard.schemas import UserCreate, UserCreateRequest
from token_guard.schemas import UserPublicResponse


class UserService:
    def __init__(
        self, user_repo: UserRepository, password_hasher: Argon2Hasher
    ) -> None:
        self._repo = user_repo
        self._hasher = password_hasher

    async def create_user(
        self, user_create_request: UserCreateRequest
    ) -> UserPublicResponse:
        email_exists = await self._repo.get_by_email(str(user_create_request.email))

        if email_exists:
            raise exception.email_already_exists

        user_create = UserCreate(
            id=str(ulid.new()),
            fullname=user_create_request.fullname,
            nickname=user_create_request.nickname,
            email=str(user_create_request.email),
            hashed_password=self._hasher.hash_password(user_create_request.password),
            role=UserRole.USER,
            created_at=datetime.now(timezone.utc),
        )
        created_user = await self._repo.create_user(user_create)

        if not created_user:
            raise exception.creation_failed_exception

        return UserPublicResponse.model_validate(created_user)

    async def get_user_by_id(self, user_id: str) -> UserPublicResponse:
        user = await self._repo.get_by_id(user_id)
        return UserPublicResponse.model_validate(user)

    async def get_user_by_email(self, email: str) -> UserPublicResponse:
        user = await self._repo.get_by_email(email)
        return UserPublicResponse.model_validate(user)
