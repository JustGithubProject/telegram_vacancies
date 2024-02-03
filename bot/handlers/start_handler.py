###############################
# Обработчик команды /start  #
###############################

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram import types

from bot.main import first_router


# Объявляем клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

# Добавляем кнопки на клавиатуру
buttons = [
    KeyboardButton(text="Я предлагаю работу"),
    KeyboardButton(text="Я ищу работу"),
]

# Добавляем кнопки на клавиатуру
keyboard.add(*buttons)


@first_router.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("Привет! Выбери нужный тебе вариант!", reply_markup=keyboard)
