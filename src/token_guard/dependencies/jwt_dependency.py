from typing import Annotated

from fastapi import Depends

from token_guard.core import config
from token_guard.services.jwt_service import JWTService


def _get_jwt_service() -> JWTService:
    jwt_service = JWTService(
        secret_key=config.SECRET_KEY,
        secret_key_access=config.SECRET_ACCESS_TOKEN,
        secret_key_refresh=config.SECRET_REFRESH_TOKEN,
        algorithm=config.ALGORITHM,
        access_expire=config.ACCESS_TOKEN_EXPIRE_MINUTES,
        refresh_expire=config.REFRESH_TOKEN_EXPIRE_DAYS,
        email_verification_expire=config.EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES,
    )
    return jwt_service


JWTServiceDep = Annotated[JWTService, Depends(_get_jwt_service)]
