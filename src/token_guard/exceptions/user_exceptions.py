from fastapi import status, HTTPException

from token_guard.constants import error_constants

email_already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail=error_constants.USER_EMAIL_ALREADY_EXISTS_ERROR,
)

creation_failed_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail=error_constants.USER_CREATION_FAILED_ERROR,
)

password_hashing_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail=error_constants.USER_PASSWORD_INVALID_ERROR,
)
