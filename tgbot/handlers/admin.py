from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter(), F.chat.type == "private")

mediagroups = {}


@admin_router.message(Command(commands='test'))
async def process_test(message: Message, state: FSMContext):
    pass
