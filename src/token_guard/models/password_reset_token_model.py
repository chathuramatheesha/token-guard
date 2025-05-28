from datetime import datetime, timezone

from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from token_guard.constants.db_constants import PASSWORD_RESET_TOKEN_TABLENAME
from token_guard.db import Base


class PasswordResetToken(Base):
    __tablename__ = PASSWORD_RESET_TOKEN_TABLENAME

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[str] = mapped_column(
        String(26),
        nullable=False,
    )
    hashed_token: Mapped[str] = mapped_column(String(110), nullable=False)
    is_used: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
