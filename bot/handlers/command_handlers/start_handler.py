###############################
# Обработчик команды /start  #
###############################
from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup
from aiogram.filters import Command
from aiogram import types

from utils.keyboards import (
    LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER
)
start_router = Router()


@start_router.message(Command(commands="start"))
async def send_welcome(message: types.Message):

    # Отправляем приветственное сообщение с клавиатурой
    await message.answer(
        "👋 Привет! Выбери нужный тебе вариант!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER,
            resize_keyboard=True
        )
    )


