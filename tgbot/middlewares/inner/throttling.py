from collections.abc import Awaitable, Callable
from typing import Any, cast, ClassVar

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message, TelegramObject
from cachetools import TTLCache


class ThrottlingMiddleware(BaseMiddleware):
    caches: ClassVar[dict[str, Any]] = {"default": TTLCache(maxsize=10_000, ttl=5)}

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        event = cast(Message, event)
        throttling_key = get_flag(data, "throttling_key")
        if throttling_key is not None and throttling_key in self.caches:
            if event.chat.id in self.caches[throttling_key]:
                await event.answer("<b>Не пишите так часто!</b>")
                return
            self.caches[throttling_key][event.chat.id] = None
        return await handler(event, data)
