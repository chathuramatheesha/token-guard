from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan():
    yield
    print("Server is shutting down...")
