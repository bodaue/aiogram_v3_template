from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.config import Config


class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, event: Message, config: Config) -> bool:
        return (event.from_user.id in config.common.admins) == self.is_admin
