"""Serviço de gerenciamento de usuários do Telegram no banco de dados."""

from agente_telegram.model.users_telegram import UsersTelegram
from agente_telegram.util.engine_postgre import DatabaseEngine
from agente_telegram.util.get_session import get_session


class UserTelegram:
    """Operações de CRUD para usuários do Telegram."""

    def __init__(self):
        self.engine = DatabaseEngine().engine

    def insert_new_user(self, id_telegram: int, full_name: str) -> bool:
        """Cadastra um novo usuário no banco de dados.

        Args:
            id_telegram: Identificador único do usuário no Telegram.
            full_name: Nome completo do usuário.

        Returns:
            True se o cadastro foi bem-sucedido, False caso contrário.
        """
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
        """Atualiza o número de telefone de um usuário existente.

        Args:
            id_telegram: Identificador único do usuário no Telegram.
            phone_number: Número de telefone a ser salvo.

        Returns:
            True se a atualização foi bem-sucedida.
        """

        with get_session(self.engine) as session:

            session.query(UsersTelegram).filter(
                UsersTelegram.id_telegram == id_telegram
                ).update(
                    {"phone_number": phone_number}
                    )

            session.commit()

        return True

    def consulta_existencia_usuario(self, id_telegram: int) -> UsersTelegram:
        """Busca um usuário pelo id_telegram.

        Args:
            id_telegram: Identificador único do usuário no Telegram.

        Returns:
            Instância de UsersTelegram correspondente.

        Raises:
            ValueError: Se o usuário não for encontrado no banco.
        """

        with get_session(self.engine) as session:

            user = session.query(UsersTelegram).filter(
                UsersTelegram.id_telegram == id_telegram
                ).first()

        if not user:
            raise ValueError("Usuário não encontrado")

        return user

    def consulta_phone_number(self, id_telegram) -> str | None:
        """Retorna o número de telefone de um usuário.

        Args:
            id_telegram: Identificador único do usuário no Telegram.

        Returns:
            Número de telefone ou None se não cadastrado.
        """

        with get_session(self.engine) as session:
            number = session.query(UsersTelegram).filter(
                UsersTelegram.id_telegram == id_telegram
                ).first()

        return number.phone_number
