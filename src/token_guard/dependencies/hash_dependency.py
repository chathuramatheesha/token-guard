from typing import Annotated

from fastapi import Depends

from token_guard.core import Argon2Hasher


def _get_argon2_hasher() -> Argon2Hasher:
    return Argon2Hasher()


def _get_argon2_hasher_refresh() -> Argon2Hasher:
    return Argon2Hasher(
        time_cost=2,
        memory_cost=16 * 1024,
        parallelism=2,
        hash_len=16,
        salt_len=16,
    )


Argon2HasherDep = Annotated[Argon2Hasher, Depends(_get_argon2_hasher)]
Argon2HasherRefreshDep = Annotated[Argon2Hasher, Depends(_get_argon2_hasher_refresh)]
