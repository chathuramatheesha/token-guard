from typing import Annotated

from fastapi import Depends

from token_guard.dependencies.db_dependeny import SessionDep
from token_guard.dependencies.hash_dependency import Argon2HasherDep
from token_guard.repositories import UserRepository
from token_guard.services.user_service import UserService


def _get_user_repository(db: SessionDep) -> UserRepository:
    return UserRepository(db)


_UserRepoDep = Annotated[UserRepository, Depends(_get_user_repository)]


def _get_user_service(repo: _UserRepoDep, hasher: Argon2HasherDep) -> UserService:
    return UserService(user_repo=repo, hasher=hasher)


UserServiceDep = Annotated[UserService, Depends(_get_user_service)]
