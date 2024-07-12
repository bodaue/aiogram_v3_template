from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from tgbot.config import Config


async def _set_default_commands(bot: Bot) -> None:
    user_commands = [BotCommand(command="start", description="Запустить бота")]
    await bot.set_my_commands(user_commands)


async def create_bot(config: Config) -> Bot:
    bot = Bot(
        token=config.common.bot_token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )
    await _set_default_commands(bot)
    return bot
