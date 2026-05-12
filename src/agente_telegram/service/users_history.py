from collections.abc import Generator
from datetime import timedelta
import logging

from sqlalchemy import func

from agente_telegram.util.get_session import (
    get_session
    )
from agente_telegram.util.engine_postgre import DatabaseEngine
from agente_telegram.model.users_history import UserHistory


class UserHistoryService:

    def __init__(self):
        self.engine = DatabaseEngine().engine

    def create_user(self, id_telegram):
        try:
            new_history = UserHistory(
                id_user=id_telegram,
                history = []
            )

            with get_session(self.engine) as session:

                session.add(new_history)

                session.commit()

            return True

        except Exception as e:
            logging.error(str(e), exc_info=True)
            return False

    def update_history(self, id_telegram, new_history):

        with get_session(self.engine) as session:
                    # Usando um nome diferente para o objeto do banco para não dar conflito
                    registro_usuario = session.query(UserHistory).filter(
                        UserHistory.id_user == id_telegram
                    ).first()

                    # Verificamos se o registro realmente existe antes de atualizar
                    if registro_usuario is not None:
                        registro_usuario.history = new_history
                        session.commit()

                    else:
                        # Caso o usuário não exista, você pode criar ou registrar um log de erro
                        logging.info(f"Erro: Tentativa de atualizar histórico de um usuário inexistente ({id_telegram})")
                        # self.create_user(id_telegram) # Opcional: tentar recriar aqui

    def consult_history(self, id_telegram):
        logging.info("consultando registro do usuário")

        with get_session(self.engine) as session:

            history = session.query(UserHistory).filter(
                UserHistory.id_user == id_telegram
            ).first()

        logging.info(f"O registro do usuário é {history}")
        if history is None:
            self.create_user(id_telegram)

            return []

        return history.history

    def yield_inactive_users_for_processing(self) -> Generator[list[UserHistory]]:
        '''Retorna os usuários a partir de um intervalo de dias'''

        logging.info(
            "consulta o histórico dos usuário a partir da data de atualização"
            )

        with get_session(self.engine) as session:

            users = session.query(UserHistory).filter(
                UserHistory.updated_at < (func.now() - timedelta(days=2)),
                UserHistory.notification_inactivity.is_(False)
            ).with_for_update(skip_locked=True).limit(20).all()

            logging.info(f'Quantidade de usuários retornado {len(users)}')

            try:
                yield users

                session.commit()

                logging.info(f'Commit realizado para {len(users)}')

            except Exception:

                session.rollback()

                logging.error('Falha no processamento')








