import uuid
from datetime import datetime, timezone

from sqlalchemy import Integer, UUID, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from token_guard.constants.db_constants import BLACKLISTED_TOKEN_TABLENAME
from token_guard.db import Base


class BlacklistedToken(Base):
    __tablename__ = BLACKLISTED_TOKEN_TABLENAME

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True, autoincrement=True
    )
    jti: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), nullable=False, default=lambda: uuid.uuid4()
    )
    reason: Mapped[str] = mapped_column(String(200), nullable=True)
    blacklisted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
