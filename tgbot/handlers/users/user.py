from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

user_router = Router()
user_router.message.filter(F.chat.type == ChatType.PRIVATE)
user_router.callback_query.filter(F.message.chat.type == ChatType.PRIVATE)


@user_router.message(CommandStart(), flags={"throttling_key": "default"})
async def user_start(message: Message, state: FSMContext):
    print(message)
    await state.clear()
