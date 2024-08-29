from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class IntIdPk:
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, auto_increment=True)
