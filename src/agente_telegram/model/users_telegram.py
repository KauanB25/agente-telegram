"""Modelo SQLAlchemy para a tabela de usuários do Telegram."""

from datetime import datetime

from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String, DateTime, func

from .base_model import Base

if TYPE_CHECKING:
    from .users_history import UserHistory


class UsersTelegram(Base):
    """Representa um usuário cadastrado via Telegram.

    Armazena o identificador do Telegram, nome completo e telefone,
    além dos timestamps de criação e última atualização.
    """

    __tablename__ = "users_telegram"

    id: Mapped[int] = mapped_column(primary_key=True)

    id_telegram: Mapped[int] = mapped_column(BigInteger)

    full_name: Mapped[str] = mapped_column(String(255))

    phone_number: Mapped[str | None] = mapped_column(String(20))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
        )

    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now()
    )

    histories: Mapped[List["UserHistory"]] = relationship(back_populates="user")
