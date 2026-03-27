from datetime import datetime

from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, func, ForeignKey, Identity, Boolean, text
from sqlalchemy.dialects.postgresql import JSONB

from .base_model import Base
from .users_telegram import UsersTelegram


class UserHistory(Base):
    __tablename__ = 'users_history'

    # id int generated always as identity primary key
    id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)

    # id_user int foreign key "user_telegram" not null
    id_user: Mapped[int] = mapped_column(ForeignKey('users_telegram.id'), nullable=False)

    # history text (sem NOT NULL, portanto aceita nulo/Optional)
    history: Mapped[Optional[str]] = mapped_column(JSONB)

    # created_at timestamptz not null
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    # updated_at timestamptz
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now() # Atualiza a data automaticamente sempre que a linha for modificada no SQLAlchemy
    )

    notification_inactivity: Mapped[Boolean] = mapped_column(
        Boolean,
        server_default=text('false'),
        nullable=False
    )

    # Relacionamento direto com a classe UserTelegram
    user: Mapped["UsersTelegram"] = relationship(back_populates="histories")
