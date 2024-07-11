import asyncio

from aiogram import Dispatcher

from tgbot.config import create_config, Config
from tgbot.factory.bot import create_bot
from tgbot.factory.dispatcher import create_dispatcher
from tgbot.factory.runners import run_polling
from tgbot.misc.logger import logger, setup_logger


async def main() -> None:
    setup_logger()
    config: Config = create_config()
    dispatcher: Dispatcher = await create_dispatcher(config)
    bot = await create_bot(config)

    return await run_polling(dispatcher=dispatcher, bot=bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Stopping bot")
