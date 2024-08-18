from typing import Any, cast, TYPE_CHECKING
from collections.abc import Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update, User

from tgbot.db.models import DBUser
from tgbot.db.repositories.user import UserRepository

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class DBUserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        event = cast(Update, event)
        aiogram_user: User = data["event_from_user"]
        session: AsyncSession = data["session"]
        repo = UserRepository(session=session)
        user = await repo.get(user_id=aiogram_user.id)

        if user is None:
            user = DBUser.from_aiogram(aiogram_user)
            await repo.create(user)
            await session.commit()

        data["db_user"] = user
        return await handler(event, data)
