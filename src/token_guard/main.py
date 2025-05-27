from fastapi import FastAPI

from token_guard.api import router
from token_guard.core.lifespan import lifespan

app = FastAPI(lifespan=lifespan)

app.include_router(router, prefix="/api")
