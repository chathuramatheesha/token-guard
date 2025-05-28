from token_guard.schemas import UserCreateRequest, UserPublicResponse
from token_guard.services.user_service import UserService


class AuthService:
    def __init__(self, user_service: UserService) -> None:
        self._user_service = user_service

    async def register_user(
        self, user_create_request: UserCreateRequest
    ) -> UserPublicResponse:
        return await self._user_service.create_user(user_create_request)
