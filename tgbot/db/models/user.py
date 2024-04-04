from datetime import datetime

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from tgbot.db.models.base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False, unique=True)
    name: Mapped[str]
    username: Mapped[str | None] = mapped_column(String(64))
    date: Mapped[datetime] = mapped_column(default=datetime.now)
