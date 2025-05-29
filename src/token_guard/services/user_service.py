from datetime import datetime, timezone

import ulid

from token_guard.core import Argon2Hasher
from token_guard.enums import UserRole
from token_guard.exceptions import user_exceptions as exceptions
from token_guard.models import User
from token_guard.repositories import UserRepository
from token_guard.schemas import UserCreate, UserCreateRequest, UserUpdateRequest


class UserService:
    def __init__(self, user_repo: UserRepository, hasher: Argon2Hasher) -> None:
        self._repo = user_repo
        self._hasher = hasher

    async def create_user(self, user_create_request: UserCreateRequest) -> User:
        email_exists = await self._repo.get_by_email(str(user_create_request.email))

        if email_exists:
            raise exceptions.user_email_already_exists

        user_create = UserCreate(
            id=str(ulid.new()),
            fullname=user_create_request.fullname,
            email=str(user_create_request.email),
            hashed_password=self._hasher.hash(user_create_request.password),
            role=UserRole.USER,
            created_at=datetime.now(timezone.utc),
        )
        created_user = await self._repo.create_user(user_create)

        if not created_user:
            raise exceptions.user_creation_failed_exception

        return created_user

    async def get_user_by_id(self, user_id: str) -> User:
        user = await self._repo.get_by_id(user_id)
        return user

    async def get_user_by_email(self, email: str) -> User:
        user = await self._repo.get_by_email(email)
        return user

    async def update_user(
        self, user_id: str, update_user_request: UserUpdateRequest
    ) -> User:
        updated_user = await self._repo.update_user(user_id, update_user_request)

        if not updated_user:
            raise exceptions.user_update_failed_exception

        return updated_user
