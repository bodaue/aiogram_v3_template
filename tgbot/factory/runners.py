from aiogram import Dispatcher, Bot

from tgbot.config import Config
from tgbot.misc.logger import logger
from tgbot.services import broadcaster


async def on_startup(bot: Bot, config: Config) -> None:
    await broadcaster.broadcast(bot, config.common.admins, "Бот запущен!")


async def on_shutdown() -> None:
    logger.info("Shutting down...")


async def run_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    dispatcher.startup.register(on_startup)
    dispatcher.shutdown.register(on_startup)
    return await dispatcher.start_polling(bot)
