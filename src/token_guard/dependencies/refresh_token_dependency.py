from typing import Annotated

from fastapi import Depends

from token_guard.dependencies.db_dependeny import SessionDep
from token_guard.dependencies.hash_dependency import Argon2HasherRefreshDep
from token_guard.repositories import RefreshTokenRepository
from token_guard.services.refresh_token_service import RefreshTokenService


def _get_refresh_token_repository(db: SessionDep) -> RefreshTokenRepository:
    repo = RefreshTokenRepository(db)
    return repo


_RefreshTokenRepoDep = Annotated[
    RefreshTokenRepository,
    Depends(_get_refresh_token_repository),
]


def _get_refresh_token_service(
    repo: _RefreshTokenRepoDep, hasher: Argon2HasherRefreshDep
) -> RefreshTokenService:
    service = RefreshTokenService(repo, hasher)
    return service


RefreshTokenServiceDep = Annotated[
    RefreshTokenService,
    Depends(_get_refresh_token_service),
]
