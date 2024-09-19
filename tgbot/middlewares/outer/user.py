from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, Any, cast

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update, User

from tgbot.db.models import DBUser
from tgbot.db.repositories.repository import Repository

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
        repo: Repository = data["repo"]
        user = await repo.users.get(user_id=aiogram_user.id)

        if user is None:
            user = DBUser.from_aiogram(aiogram_user)
            await repo.users.create(user)
            await session.commit()

        data["db_user"] = user
        return await handler(event, data)
