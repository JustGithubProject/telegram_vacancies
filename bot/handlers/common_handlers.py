#########################################################################
# Общие обработчики, например, обработчик для неопознанных команд.      #
#########################################################################
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

from utils.helpers import MyStates


# Объявляем клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

# Добавляем кнопки на клавиатуру
buttons = [
    KeyboardButton(text="Смотреть резюме"),
    KeyboardButton(text="Создать вакансию"),
]

# Добавляем кнопки на клавиатуру
keyboard.add(*buttons)


async def process_choice(message: types.Message, state: FSMContext):
    if message.text == "Я предлагаю работу":
        await message.answer("Вы выбрали: Я предлагаю работу", reply_markup=keyboard)
    elif message.text == "Я ищу работу":
        await message.answer("Вы выбрали: Я ищу работу")

    await state.finish()