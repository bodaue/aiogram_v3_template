from __future__ import annotations

from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from redis.asyncio import Redis

from ..config import Config
from ..handlers.admins.admin import admin_router
from ..handlers.users.user import user_router
from ..middlewares.throttling import ThrottlingMiddleware


def _setup_outer_middlewares(dispatcher: Dispatcher, config: Config) -> None:  # noqa
    pass


def _setup_inner_middlewares(dispatcher: Dispatcher) -> None:
    dispatcher.message.middleware(ThrottlingMiddleware())
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware())


def _setup_routers(dispatcher: Dispatcher) -> None:
    dispatcher.include_routers(user_router, admin_router)


async def create_dispatcher(config: Config) -> Dispatcher:
    """
    :return: Configured ``Dispatcher`` with installed middlewares and included routers
    """
    storage: BaseStorage
    if config.redis.use_redis:
        storage = RedisStorage(
            Redis(
                host=config.redis.host,
                port=config.redis.port,
                password=config.redis.password,
            )
        )
    else:
        storage = MemoryStorage()

    dispatcher: Dispatcher = Dispatcher(
        name="main_dispatcher",
        storage=storage,
        config=config,
    )
    _setup_outer_middlewares(dispatcher=dispatcher, config=config)
    _setup_inner_middlewares(dispatcher=dispatcher)

    _setup_routers(dispatcher=dispatcher)
    return dispatcher
