from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

user_router = Router()
user_router.message.filter(F.chat.type == "private")
user_router.callback_query.filter(F.message.chat.type == 'private')


@user_router.message(CommandStart(), flags={'throttling_key': 'default'})
async def user_startg(message: Message, state: FSMContext):
    await state.clear()
