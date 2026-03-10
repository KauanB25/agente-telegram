from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, String, DateTime, func


class Base(DeclarativeBase):
    pass


class UsersTelegram(Base):
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
