###############################
# Обработчик команды /start  #
###############################

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import types

# Объявляем клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

# Добавляем кнопки на клавиатуру
buttons = [
    KeyboardButton(text="Я предлагаю работу"),
    KeyboardButton(text="Я ищу работу"),
]

# Добавляем кнопки на клавиатуру
keyboard.add(*buttons)


async def send_welcome(message: types.Message):
    await message.answer("Привет! Выбери нужный тебе вариант!", reply_markup=keyboard)