from __future__ import annotations

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from tgbot.db.models import Base
from tgbot.db.models.mixins import TimestampMixin
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiogram.types import User


class DBUser(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    name: Mapped[str]
    username: Mapped[str | None] = mapped_column(String(64))

    @classmethod
    def from_aiogram(cls, user: User) -> DBUser:
        return cls(id=user.id, name=user.full_name, username=user.username)
