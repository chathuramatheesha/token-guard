from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from token_guard.db import get_db

SessionDep = Annotated[AsyncSession, Depends(get_db)]
