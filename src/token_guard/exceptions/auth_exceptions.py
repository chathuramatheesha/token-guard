from fastapi import HTTPException, status

from token_guard.constants import error_constants

auth_invalid_credentials_exception = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail=error_constants.AUTH_INVALID_CREDENTIALS,
)
