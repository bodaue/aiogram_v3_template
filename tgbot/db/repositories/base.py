from abc import abstractmethod, ABC
from collections.abc import Sequence
from typing import TypeVar, Generic, Any

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import Base

T = TypeVar("T", bound=Base)


class AbstractRepository(Generic[T], ABC):
    @abstractmethod
    async def get_by_id(self, _id: int) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, **filters: Any) -> T | None:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, **filters: Any) -> Sequence[T]:
        raise NotImplementedError

    @abstractmethod
    async def create(self, instance: T) -> T:
        raise NotImplementedError

    @abstractmethod
    async def update(self, instance: T) -> T:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, _id: int) -> None:
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository[T]):
    def __init__(self, session: AsyncSession, model: type[T]) -> None:
        self._session = session
        self.model = model

    async def get_by_id(self, _id: int) -> T | None:
        return await self._session.get(self.model, _id)

    async def get_one(self, **filters: Any) -> T | None:
        return await self._session.scalar(select(self.model).filter_by(**filters))

    async def get_all(self, **filters: Any) -> Sequence[T]:
        return (
            await self._session.scalars(select(self.model).filter_by(**filters))
        ).all()

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
