from aiogram import F, Router
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
from tgbot.misc.logger import logger

admin_router = Router()
admin_router.message.filter(AdminFilter(), F.chat.type == ChatType.PRIVATE)
admin_router.callback_query.filter(
    AdminFilter(),
    F.message.chat.type == ChatType.PRIVATE,
)


@admin_router.message(Command(commands="test"))
async def process_test(message: Message, state: FSMContext):
    logger.info(message)
    await state.clear()
