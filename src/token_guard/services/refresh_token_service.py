from token_guard.core import Argon2Hasher
from token_guard.exceptions import token_exceptions as exceptions
from token_guard.models import RefreshToken
from token_guard.repositories import RefreshTokenRepository
from token_guard.schemas import RefreshTokenSave


class RefreshTokenService:
    def __init__(self, repo: RefreshTokenRepository, hasher: Argon2Hasher):
        self._repo = repo
        self._hasher = hasher

    async def save_refresh_token(
        self, refresh_token_save: RefreshTokenSave
    ) -> RefreshToken:
        refresh_token_save.hashed_token = self._hasher.hash(
            refresh_token_save.hashed_token
        )
        saved_refresh_token = await self._repo.save_token(refresh_token_save)

        if not saved_refresh_token:
            raise exceptions.token_refresh_save_exception

        return saved_refresh_token
