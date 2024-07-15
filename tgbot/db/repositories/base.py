from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import Base


class BaseRepository:
    _session: AsyncSession

    def __init__(self, session: AsyncSession):
        self._session = session

    async def create(self, obj: Base) -> None:
        self._session.add(obj)
        await self._session.commit()

    async def delete(self, obj: Base) -> None:
        await self._session.delete(obj)
        await self._session.commit()
