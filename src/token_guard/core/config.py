from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    APP_NAME: str | None = None
    APP_VERSION: str | None = None
    APP_LINK: str | None = None

    SECRET_KEY: str | None = None
    SECRET_REFRESH_TOKEN: str | None = None
    SECRET_ACCESS_TOKEN: str | None = None
    SECURITY_PASSWORD_SALT: str | None = None
    ALGORITHM: str | None = None

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10
    EMAIL_VERIFICATION_TOKEN_EXPIRE_MINUTES: int = 10
    REFRESH_TOKEN_EXPIRE_DAYS: int = 3

    DATABASE_URL: str | None = None
    DATABASE_ECHO: bool = False
    DATABASE_ROLLBACK: bool = True

    GMAIL_USERNAME: str | None = None
    GMAIL_APP_PASSWORD: str | None = None

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


config = BaseConfig()
