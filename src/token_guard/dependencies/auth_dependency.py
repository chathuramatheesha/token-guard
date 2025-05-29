from typing import Annotated

from fastapi import Depends

from token_guard.dependencies.email_dependency import EmailServiceDep
from token_guard.dependencies.hash_dependency import Argon2HasherDep
from token_guard.dependencies.jwt_dependency import JWTServiceDep
from token_guard.dependencies.refresh_token_dependency import RefreshTokenServiceDep
from token_guard.dependencies.user_dependency import UserServiceDep
from token_guard.services import AuthService


async def _get_auth_service(
    user_service: UserServiceDep,
    jwt_service: JWTServiceDep,
    refresh_token_service: RefreshTokenServiceDep,
    email_service: EmailServiceDep,
    password_hasher: Argon2HasherDep,
) -> AuthService:
    auth_service = AuthService(
        user_service=user_service,
        jwt_service=jwt_service,
        refresh_token_service=refresh_token_service,
        email_service=email_service,
        hasher=password_hasher,
    )
    return auth_service


AuthServiceDep = Annotated[AuthService, Depends(_get_auth_service)]
