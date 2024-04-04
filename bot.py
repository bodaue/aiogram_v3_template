import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from tgbot.config import config
from tgbot.handlers.admin import admin_router
from tgbot.handlers.user import user_router
from tgbot.middlewares.throttling import ThrottlingMiddleware
from tgbot.misc.set_bot_commands import set_default_commands
from tgbot.services import broadcaster

logger = logging.getLogger(__name__)
log_level = logging.INFO
bl.basic_colorized_config(level=log_level)


async def on_startup(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "Бот запущен!")


async def on_shutdown():
    print('Shutting down...')


def register_global_middlewares(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())
    dp.callback_query.middleware(CallbackAnswerMiddleware())


def register_logger():
    logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-6s [%(asctime)s]  %(message)s',
                        datefmt='%d.%m.%Y %H:%M:%S',
                        level=log_level)
    logger.info("Starting bot")


async def main():
    register_logger()

    storage = MemoryStorage()

    bot = Bot(token=config.common.bot_token.get_secret_value(),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)
    dp.include_routers(user_router,
                       admin_router)

    register_global_middlewares(dp=dp)

    await set_default_commands(bot)

    await on_startup(bot, config.common.admins)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot, config=config, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Stopping bot")
