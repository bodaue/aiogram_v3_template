from typing import Callable, Awaitable, Dict, Any, Optional

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User, Update
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import DBUser


class DBUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        aiogram_user: Optional[User] = data.get("event_from_user")
        session: AsyncSession = data.get("session")
        user = await session.get(DBUser, aiogram_user.id)

        if user is None:
            user = DBUser.from_aiogram(aiogram_user)
            session.add(user)
            await session.commit()

        data["db_user"] = user
        return await handler(event, data)
