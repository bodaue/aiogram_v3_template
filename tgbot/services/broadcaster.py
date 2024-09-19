import asyncio
import logging
from collections.abc import Iterable

from aiogram import Bot, exceptions


async def send_message(
    bot: Bot,
    user_id: int,
    text: str,
    disable_notification: bool = False,
) -> bool:
    try:
        await bot.send_message(user_id, text, disable_notification=disable_notification)
    except exceptions.TelegramForbiddenError:
        logging.exception("Target [ID:%d]: got TelegramForbiddenError", user_id)
    except exceptions.TelegramRetryAfter as e:
        logging.exception(
            "Target [ID:%d]: Flood limit is exceeded. Sleep %d seconds.",
            user_id,
            e.retry_after,
        )
        await asyncio.sleep(e.retry_after)
        return await send_message(bot, user_id, text)  # Recursive call
    except exceptions.TelegramAPIError:
        logging.exception("Target [ID:%d]: failed", user_id)
    else:
        logging.info("Target [ID:%d]: success", user_id)
        return True
    return False


async def broadcast(bot: Bot, users: Iterable[int], text: str) -> int:
    """Simple broadcaster
    :return: Count of messages.
    """
    count = 0
    try:
        for user_id in users:
            if await send_message(bot, user_id, text):
                count += 1
            await asyncio.sleep(
                0.05,
            )  # 20 messages per second (Limit: 30 messages per second)
    finally:
        logging.info("%d messages successful sent.", count)

    return count
