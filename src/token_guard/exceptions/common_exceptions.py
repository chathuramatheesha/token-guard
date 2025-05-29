from fastapi import HTTPException, status

from token_guard.constants import error_constants

dataclass_invalid_exception = TypeError(error_constants.DATACLASS_INVALID_ERROR)

email_missing_field_exception = HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail=error_constants.EMAIL_MISSING_FIELDS_ERROR,
)
