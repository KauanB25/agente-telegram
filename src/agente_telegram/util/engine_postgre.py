from sqlalchemy import create_engine, Engine
from agente_telegram.config.settings import settings


class DatabaseEngine:
    _instance: 'DatabaseEngine | None' = None

    _engine: Engine | None = None

    def __new__(cls) -> 'DatabaseEngine':
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._create_engine()

        return cls._instance

    @classmethod
    def _create_engine(cls):

        url_db = (
            f"{settings.db_postgree_driver}://"
            f"{settings.db_postgree_user}:"
            f"{settings.db_postgree_secret.get_secret_value()}@"
            f"{settings.db_postgree_host}:"
            f"{settings.db_postgree_port}/"
            f"{settings.db_postgree_database}"
        )

        cls._engine = create_engine(url_db)

    @property
    def engine(self) -> Engine:
        return self._engine
