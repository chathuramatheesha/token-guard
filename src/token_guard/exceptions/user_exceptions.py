from fastapi import status, HTTPException

from token_guard.constants import error_constants

user_email_already_exists = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail=error_constants.USER_EMAIL_ALREADY_EXISTS_ERROR,
)

user_creation_failed_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail=error_constants.USER_CREATION_FAILED_ERROR,
)

user_update_failed_exception = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail=error_constants.USER_UPDATE_FAILED_ERROR,
)

user_password_hashing_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail=error_constants.USER_PASSWORD_INVALID_ERROR,
)

user_id_not_exists = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=error_constants.USER_ID_NOT_EXISTS_ERROR,
)

user_email_not_exists = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=error_constants.USER_EMAIL_NOT_EXISTS_ERROR,
)
