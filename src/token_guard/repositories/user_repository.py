from typing import Sequence

from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from token_guard.models import User
from token_guard.schemas import UserCreate, UserUpdateRequest


class UserRepository:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    async def get_by_id(self, user_id: str) -> User | None:
        stmt = select(User).where(User.id == user_id)
        user = await self._db.scalar(stmt)
        return user

    async def get_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        user = await self._db.scalar(stmt)
        return user

    async def create_user(self, user_create: UserCreate) -> User:
        stmt = insert(User).values(**user_create.model_dump()).returning(User)
        inserted_user = await self._db.scalar(stmt)
        await self._db.commit()
        return inserted_user

    async def update_user(self, user_id: str, user_update: UserUpdateRequest) -> User:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(**user_update.model_dump(exclude_unset=True))
            .returning(User)
        )
        updated_user = await self._db.scalar(stmt)
        await self._db.commit()
        return updated_user

    async def delete_user(self, user_id: str) -> None:
        stmt = delete(User).where(User.id == user_id)
        await self._db.execute(stmt)
        await self._db.commit()
        return

    async def deactivate_user(self, user_id: str) -> User:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(is_active=False)
            .returning(User)
        )
        deactivated_user = await self._db.scalar(stmt)
        await self._db.commit()
        return deactivated_user

    async def set_password(self, user_id: str, hashed_password: str) -> User:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(hashed_password=hashed_password)
            .returning(User)
        )
        updated_user = await self._db.scalar(stmt)
        await self._db.commit()
        return updated_user

    async def verify_email(self, user_id: str) -> User:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(is_verified=True)
            .returning(User)
        )
        verified_user = await self._db.scalar(stmt)
        await self._db.commit()
        return verified_user

    async def list_user(self) -> Sequence[User]:
        stmt = select(User)
        users = await self._db.scalars(stmt)
        return users.all()
