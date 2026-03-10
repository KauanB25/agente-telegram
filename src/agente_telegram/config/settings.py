from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr


class Settings(BaseSettings):
    token_telegram: SecretStr = Field(
        ...,
        alias='TOKEN_TELEGRAM',
        description="Token para comunicação com o telegram")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
