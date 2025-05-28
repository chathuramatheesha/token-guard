from enum import Enum


class UserRole(str, Enum):
    GUEST = "guest"
    USER = "user"
    EXCLUSIVE = "exclusive"
    MODERATOR = "moderator"
    ADMIN = "admin"
