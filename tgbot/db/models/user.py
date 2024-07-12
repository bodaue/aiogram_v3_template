from __future__ import annotations

from aiogram.types import User
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from tgbot.db.models.base import Base, TimestampMixin


class DBUser(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, autoincrement=False, unique=True
    )
    name: Mapped[str]
    username: Mapped[str | None] = mapped_column(String(64))

    @classmethod
    def from_aiogram(cls, user: User) -> DBUser:
        return cls(id=user.id, name=user.full_name, username=user.username)
