from fastapi import HTTPException, status

from token_guard.constants import error_constants

token_refresh_save_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail=error_constants.TOKEN_REFRESH_SAVE_FAILED_ERROR,
)

jwt_credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=error_constants.JWT_CREDENTIALS_INVALID,
    headers={"WWW-Authenticate": "Bearer"},
)

jwt_token_expired_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=error_constants.JWT_TOKEN_EXPIRED,
)

jwt_token_invalid_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail=error_constants.JWT_TOKEN_INVALID,
)
