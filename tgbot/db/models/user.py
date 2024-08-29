from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from tgbot.db.models import Base
from tgbot.db.models.mixins import TimestampMixin
from tgbot.db.models.mixins.int_id_pk import IntIdPk

if TYPE_CHECKING:
    from aiogram.types import User


class DBUser(IntIdPk, TimestampMixin, Base):
    __tablename__ = "users"

    name: Mapped[str]
    username: Mapped[str | None] = mapped_column(String(64))

    @classmethod
    def from_aiogram(cls, user: User) -> DBUser:
        return cls(id=user.id, name=user.full_name, username=user.username)
