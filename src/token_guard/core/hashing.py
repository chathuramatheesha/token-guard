from argon2 import Type, PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHash

from token_guard.exceptions import user_exceptions


class Argon2Hasher:
    def __init__(
        self,
        time_cost: int = 3,
        memory_cost: int = 64 * 1024,
        parallelism: int = 2,
        hash_len: int = 32,
        salt_len: int = 16,
        type_: Type = Type.ID,
    ) -> None:
        self._hasher = PasswordHasher(
            time_cost=time_cost,
            memory_cost=memory_cost,
            parallelism=parallelism,
            hash_len=hash_len,
            salt_len=salt_len,
            type=type_,
        )

    def hash_password(self, password: str) -> str:
        if not password or not isinstance(password, str):
            raise user_exceptions.password_hashing_exception

        return self._hasher.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        try:
            return self._hasher.verify(hashed_password, plain_password)
        except (VerifyMismatchError, VerificationError, InvalidHash):
            return False

    def needs_rehash(self, hashed_password: str) -> bool:
        return self._hasher.check_needs_rehash(hashed_password)
