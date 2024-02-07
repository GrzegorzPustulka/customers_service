from functools import lru_cache

from pydantic import PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8")

    # DATABASE
    db_user: str = "postgres"
    db_password: SecretStr = SecretStr("SecretPassword_1!")
    db_host: str = "localhost"
    db_port: str = "5432"
    db_name: str = "DineStream"

    @property
    def sqlalchemy_database_uri(self) -> PostgresDsn:
        return f"postgresql://{self.db_user}:{self.db_password.get_secret_value()}@{self.db_host}:{self.db_port}/{self.db_name}"

    # SMTP
    smtp_server: str = "localhost"
    smtp_port: int = 1025
    sender_email: str = "test@example.com"
    smtp_password: SecretStr = SecretStr("")


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
