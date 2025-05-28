from typing import Annotated

from fastapi import Depends

from token_guard.core import Argon2Hasher
from token_guard.dependencies.db_dependeny import SessionDep
from token_guard.repositories import UserRepository
from token_guard.services.auth_service import AuthService
from token_guard.services.user_service import UserService


async def _get_auth_service(db: SessionDep) -> AuthService:
    user_service = UserService(
        user_repo=UserRepository(db),
        password_hasher=Argon2Hasher(),
    )
    auth_service = AuthService(
        user_service=user_service,
    )
    return auth_service


AuthServiceDep = Annotated[AuthService, Depends(_get_auth_service)]
