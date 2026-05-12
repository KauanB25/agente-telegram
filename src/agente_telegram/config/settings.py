"""Módulo de configuração da aplicação via variáveis de ambiente."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr


class Settings(BaseSettings):
    """Configurações da aplicação carregadas automaticamente do arquivo .env.

    Utiliza pydantic-settings para validação de tipos e carregamento
    de variáveis de ambiente com suporte a aliases e valores padrão.
    """
    token_telegram: SecretStr = Field(
        ...,
        alias='TOKEN_TELEGRAM',
        description="Token para comunicação com o telegram"
        )

    db_postgree_host: str = Field(
        default="localhost",
        description="Servidor que hospeda o banco de dados"
        )

    db_postgree_port: int = Field(
        default='5432',
        description="porta do banco",
        alias="DB_POSTGREE_PORT"
        )

    db_postgree_user: str = Field(
        ...,
        description="Usuário para conexão",
        alias="DB_POSTGREE_USER"
        )

    db_postgree_database: str = Field(
        ...,
        description="Nome do banco",
        alias="DB_POSTGREE_DATABASE"
        )

    db_postgree_secret: SecretStr = Field(
        ...,
        description="Senha do banco",
        alias="DB_POSTGREE_PASSWORD"
        )

    db_postgree_driver: str = Field(
        default="postgresql",
        description="Driver de comunicação"
        )

    alembic_table_version: str = Field(
        default="alembic_version",
        description="Nome da tabela que armazena a versão atual do banco"
        )

    google_gemini_api_key: str = Field(
        ...,
        alias="GOOGLE_GEMINI_API_KEY",
        description="Api do google para comunicar com o gemini"
    )

    url_webhook: str =  Field(
        ...,
        alias='URL_WEBHOOK',
        description="URL para qual o telegram irá enviar as requisições")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
