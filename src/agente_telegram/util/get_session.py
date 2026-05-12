"""Módulo utilitário para gerenciamento de sessões do SQLAlchemy."""

from contextlib import contextmanager

from sqlalchemy import Engine
from sqlalchemy.orm import Session


@contextmanager
def get_session(engine: Engine):
    """Context manager que fornece uma sessão transacional do SQLAlchemy.

    Realiza rollback automático em caso de exceção e garante
    o fechamento da sessão ao final do bloco.

    Args:
        engine: Engine SQLAlchemy utilizada para criar a sessão.

    Yields:
        Session: Sessão ativa do SQLAlchemy.

    Raises:
        Exception: Re-levanta qualquer exceção após executar rollback.
    """

    with Session(engine) as session:
        try:
            yield session
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
