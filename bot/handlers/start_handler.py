###############################
# Обработчик команды /start  #
###############################
from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram import types

start_router = Router()


@start_router.message(Command(commands="start"))
async def send_welcome(message: types.Message):

    # Отправляем приветственное сообщение с клавиатурой
    await message.answer(
        "👋 Привет! Выбери нужный тебе вариант!",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="1️⃣ Я предлагаю работу"),
                    KeyboardButton(text="2️⃣ Я ищу работу"),
                ]
            ],
            resize_keyboard=True
        )
    )
