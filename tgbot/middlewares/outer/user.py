from typing import Callable, Awaitable, Dict, Any, cast

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User, Update
from sqlalchemy.ext.asyncio import AsyncSession

from tgbot.db.models import DBUser


class DBUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        event = cast(Update, event)
        aiogram_user: User = data["event_from_user"]
        session: AsyncSession = data["session"]
        user = await session.get(DBUser, aiogram_user.id)

        if user is None:
            user = DBUser.from_aiogram(aiogram_user)
            session.add(user)
            await session.commit()

        data["db_user"] = user
        return await handler(event, data)
