from contextlib import asynccontextmanager

from fastapi import FastAPI

from token_guard.db.init import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    print("Server is shutting down...")
