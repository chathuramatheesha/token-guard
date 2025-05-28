from datetime import datetime, timezone

from sqlalchemy import Integer, String, TEXT, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from token_guard.constants.db_constants import REFRESH_TOKEN_TABLENAME
from token_guard.db import Base


class RefreshToken(Base):
    __tablename__ = REFRESH_TOKEN_TABLENAME

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True, index=True
    )
    jti: Mapped[str] = mapped_column(
        String(26), nullable=False, unique=True, index=True
    )
    user_id: Mapped[str] = mapped_column(String(26), nullable=False)
    hashed_token: Mapped[str] = mapped_column(String(110), nullable=False)
    ip_address: Mapped[str] = mapped_column(String(45), nullable=False)
    device_info: Mapped[str] = mapped_column(TEXT, nullable=True)
    is_backlisted: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
