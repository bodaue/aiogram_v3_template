from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

test_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="test", url="test.com")]],
)
