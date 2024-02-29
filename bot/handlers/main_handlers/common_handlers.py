#########################################################################
# Общие обработчики, например, обработчик для неопознанных команд.      #
#########################################################################
from aiogram import (
    Router,
    types,
    F
)
from aiogram.types import ForceReply

from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
)

from utils.keyboards import (
    LIST_KEYBOARD_BUTTONS_FOR_COMMON_HANDLER_FIRST_OPTION,
    LIST_KEYBOARD_BUTTONS_FOR_COMMON_HANDLER_SECOND_OPTION,
    LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER
)


# router for handlers
common_router = Router()


@common_router.message()
async def process_choice(message: types.Message):
    """Обработка первой клавиатуры бота"""
    if message.text == "1️⃣ Я предлагаю работу":
        await message.answer("✅ Вы выбрали: Я предлагаю работу", reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_COMMON_HANDLER_FIRST_OPTION,
            resize_keyboard=True
        )
    )

    elif message.text == "2️⃣ Я ищу работу":
        await message.answer("✅ Вы выбрали: Я ищу работу", reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_COMMON_HANDLER_SECOND_OPTION,
            resize_keyboard=True
        )
    )

