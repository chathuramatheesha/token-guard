from dataclasses import asdict
from typing import Sequence

from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from token_guard.models.refresh_token_model import RefreshToken
from token_guard.schemas.token_schemas import RefreshTokenSave


class RefreshTokenRepository:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def save_token(self, refresh_token_save: RefreshTokenSave) -> RefreshToken:
        stmt = (
            insert(RefreshToken)
            .values(asdict(refresh_token_save))
            .returning(RefreshToken)
        )
        refresh_token = await self._db.scalar(stmt)
        await self._db.commit()
        return refresh_token

    async def get_by_jti(self, jti: str) -> RefreshToken:
        stmt = select(RefreshToken).where(RefreshToken.jti == jti)
        refresh_token = await self._db.scalar(stmt)
        return refresh_token

    async def list_tokens_by_user_id(self, user_id: str) -> Sequence[RefreshToken]:
        stmt = select(RefreshToken).where(RefreshToken.user_id == user_id)
        result = await self._db.scalars(stmt)
        return result.all()

    async def delete_token(self, jti: str) -> None:
        stmt = delete(RefreshToken).where(RefreshToken.jti == jti)
        await self._db.execute(stmt)
        await self._db.commit()
        return
