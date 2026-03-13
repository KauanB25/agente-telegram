from agente_telegram.model.users_telegram import UsersTelegram
from agente_telegram.util.engine_postgre import create_engine_postgre
from agente_telegram.config.settings import settings
from agente_telegram.util.get_session import get_session


class UserTelegram:

    def __init__(self):
        self.engine = create_engine_postgre(
            settings.db_postgree_user,
            settings.db_postgree_secret.get_secret_value(),
            settings.db_postgree_host,
            settings.db_postgree_database,
            settings.db_postgree_driver
            )

    def insert_new_user(self, id_telegram: int, full_name: str) -> bool:
        try:
            new_user = UsersTelegram(
                id_telegram=id_telegram,
                full_name=full_name
            )

            with get_session(self.engine) as session:

                session.add(new_user)

                session.commit()

            return True

        except Exception:
            return False

    def update_user_phone(self, id_telegram: int, phone_number: str):

        with get_session(self.engine) as session:

            session.query(UsersTelegram).filter(
                UsersTelegram.id_telegram == id_telegram
                ).update(
                    {"phone_number": phone_number}
                    )

            session.commit()

        return True

    def consulta_existencia_usuario(self, id_telegram: int) -> UsersTelegram:

        with get_session(self.engine) as session:

            user = session.query(UsersTelegram).filter(
                UsersTelegram.id_telegram == id_telegram
                ).first()

        if not user:
            raise ValueError("Usuário não encontrado")

        return user

    def consulta_phone_number(self, id_telegram) -> str | None:

        with get_session(self.engine) as session:
            number = session.query(UsersTelegram).filter(
                UsersTelegram.id_telegram == id_telegram
                ).first()

        return number.phone_number
