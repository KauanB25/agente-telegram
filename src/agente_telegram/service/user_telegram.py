from sqlalchemy.orm import Session

from agente_telegram.model.users_telegram import UsersTelegram
from agente_telegram.util.engine_postgre import create_engine_postgre
from agente_telegram.config.settings import settings


class UserTelegram:

    def __init__(self):
        self.engine = create_engine_postgre(
            settings.db_postgree_user,
            settings.db_postgree_secret,
            settings.db_postgree_host,
            settings.db_postgree_database,
            settings.db_postgree_driver
            )

    def _session(self, usuario: UsersTelegram):

        with Session(self.engine) as session:

            new_user = usuario

            session.add(new_user)

            session.commit()

    def insert_new_user(self, id_telegram, full_name):

        try:

            new_user = UsersTelegram(
                id_telegram=id_telegram,
                full_name=full_name
            )

            self._session(new_user)

            return True

        except Exception:
            return False

    def consulta_existencia_usuario(self):
        pass
