from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from tgbot.config import Config
from tgbot.misc.set_bot_commands import set_default_commands


async def create_bot(config: Config) -> Bot:
    bot = Bot(
        token=config.common.bot_token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )
    await set_default_commands(bot)
    return bot
