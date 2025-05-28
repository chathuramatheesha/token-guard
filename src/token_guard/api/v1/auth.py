from fastapi import APIRouter, status

from token_guard.dependencies import AuthServiceDep
from token_guard.schemas import UserPublicResponse, UserCreateRequest

router = APIRouter()


@router.post(
    "/register",
    status_code=status.HTTP_200_OK,
    response_model=UserPublicResponse,
)
async def register(
    user_create_request: UserCreateRequest,
    service: AuthServiceDep,
) -> UserPublicResponse:
    return await service.register_user(user_create_request)


# @router.post('/login', status_code=status.HTTP_200_OK, response_model=A)
