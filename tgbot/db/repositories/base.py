from abc import abstractmethod, ABC
from typing import TypeVar, Generic, Type, Sequence

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import Base

T = TypeVar("T", bound=Base)


class AbstractRepository(Generic[T], ABC):
    @abstractmethod
    async def get_by_id(self, _id: int) -> T | None:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self, **filters) -> list[T]:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, instance: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, instance: T) -> T:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, _id: int) -> None:
        raise NotImplementedError()


class SQLAlchemyRepository(AbstractRepository[T]):
    def __init__(self, session: AsyncSession, model: Type[T]) -> None:
        self._session = session
        self.model = model

    async def get_by_id(self, _id: int) -> T | None:
        return await self._session.get(self.model, _id)

    async def get_all(self, **filters) -> Sequence[T]:
        return (await self._session.scalars(select(self.model).where(**filters))).all()

    async def create(self, instance: T) -> T:
        self._session.add(instance)
        await self._session.flush()
        await self._session.refresh(instance)
        return instance

    async def update(self, instance: T) -> T:
        self._session.add(instance)
        await self._session.flush()
        await self._session.refresh(instance)
        return instance

    async def delete(self, _id: int) -> None:
        stmt = delete(self.model).where(self.model.id == _id)
        await self._session.execute(stmt)
