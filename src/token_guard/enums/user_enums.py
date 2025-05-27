from enum import Enum


class UserRole(Enum):
    GUEST = "guest"
    USER = "user"
    EXCLUSIVE = "exclusive"
    MODERATOR = "moderator"
    ADMIN = "admin"
