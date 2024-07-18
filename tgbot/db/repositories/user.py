from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import DBUser
from tgbot.db.repositories.base import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository[DBUser]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, DBUser)

    async def get(self, user_id: int) -> DBUser | None:
        return await super().get_by_id(user_id)
