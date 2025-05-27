from datetime import datetime, timezone

from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from token_guard.constants.db_constants import EMAIL_VERIFICATION_TOKEN_TABLENAME
from token_guard.db import Base


class EmailVerificationToken(Base):
    __tablename__ = EMAIL_VERIFICATION_TOKEN_TABLENAME

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    hashed_token: Mapped[str] = mapped_column(String(110), nullable=False)
    is_used: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
