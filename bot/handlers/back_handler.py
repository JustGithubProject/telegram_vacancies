from aiogram import (
    types,
    Router,
    F
)
from aiogram.types import ReplyKeyboardMarkup

from utils.keyboards import LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER

back_router = Router()


@back_router.message(F.text == "🔙 НАЗАД")
async def back_handler(message: types.Message):
    print("BACK")
    await message.answer(
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER,
            resize_keyboard=True
            )
        )


