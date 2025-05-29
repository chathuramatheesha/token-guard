# USER ERROR MESSAGES
USER_EMAIL_ALREADY_EXISTS_ERROR = "User with this email already exists."
USER_CREATION_FAILED_ERROR = "Failed to create user due to server error."
USER_UPDATE_FAILED_ERROR = "Failed to update user due to server error."
USER_PASSWORD_INVALID_ERROR = "Password must be a non-empty string."
USER_ID_NOT_EXISTS_ERROR = "User with the provided ID does not exist."
USER_EMAIL_NOT_EXISTS_ERROR = "User with the provided email does not exist."

# AUTH ERROR MESSAGES
AUTH_INVALID_CREDENTIALS = "Invalid email or password."

# JWT ERROR MESSAGES
JWT_CREDENTIALS_INVALID = "Could not validate credentials."
JWT_TOKEN_EXPIRED = "Token expired."
JWT_TOKEN_INVALID = "Token invalid."
JWT_INVALID_TOKEN_TYPE = "Token type invalid."

# TOKEN ERROR MESSAGES
TOKEN_REFRESH_SAVE_FAILED_ERROR = (
    "Failed to store refresh token. Please try again later."
)

# COMMON ERROR MESSAGES
DATACLASS_INVALID_ERROR = "{} must be a dataclass"
EMAIL_MISSING_FIELDS_ERROR = (
    "Missing one or more required email fields: subject, from, to, content"
)
