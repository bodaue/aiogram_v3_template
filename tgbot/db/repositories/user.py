from tgbot.db.models import DBUser
from tgbot.db.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def get(self, user_id: int) -> DBUser | None:
        return await self._session.get(DBUser, user_id)
