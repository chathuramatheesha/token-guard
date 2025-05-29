from fastapi import APIRouter, status, Request, Response, BackgroundTasks

from token_guard.dependencies import AuthServiceDep
from token_guard.enums import TokenType
from token_guard.schemas import (
    UserPublicResponse,
    UserCreateRequest,
    AuthLoginResponse,
    AuthLoginRequest,
)
from token_guard.utils.token_utils import refresh_token_max_age

router = APIRouter()


@router.post(
    "/register",
    status_code=status.HTTP_200_OK,
    response_model=UserPublicResponse,
)
async def register(
    user_create_request: UserCreateRequest,
    service: AuthServiceDep,
    background_tasks: BackgroundTasks,
) -> UserPublicResponse:
    return await service.register_user(user_create_request, background_tasks)


@router.post("/login", status_code=status.HTTP_200_OK, response_model=AuthLoginResponse)
async def login(
    request: Request,
    response: Response,
    user_login_reqeust: AuthLoginRequest,
    service: AuthServiceDep,
) -> AuthLoginResponse:
    tokens = await service.login(request, user_login_reqeust)
    response.set_cookie(
        key=TokenType.REFRESH_TOKEN.value,
        value=tokens.refresh_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=refresh_token_max_age(),
    )
    return tokens
