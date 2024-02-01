#########################################################################
# Общие обработчики, например, обработчик для неопознанных команд.      #
#########################################################################
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

from utils.helpers import MyStates


# Объявляем клавиатуру
keyboard_first = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_second = ReplyKeyboardMarkup(resize_keyboard=True)

# Добавляем кнопки на клавиатуру
buttons_first = [
    KeyboardButton(text="Смотреть резюме"),
    KeyboardButton(text="Создать вакансию"),
]

buttons_second = [
    KeyboardButton(text="Смотреть вакансии"),
    KeyboardButton(text="Создать резюме")
]

# Добавляем кнопки на клавиатуру
keyboard_first.add(*buttons_first)
keyboard_second.add(*buttons_second)


async def process_choice(message: types.Message, state: FSMContext):
    if message.text == "Я предлагаю работу":
        await message.answer("Вы выбрали: Я предлагаю работу", reply_markup=keyboard_first)
        #await state.update_data(choice=message.text)
        #await MyStates.choice.set()
    elif message.text == "Я ищу работу":
        await message.answer("Вы выбрали: Я ищу работу", reply_markup=keyboard_second)

    # Сохраняем состояние выбора пользователя
    await state.update_data(choice=message.text)
    await state.finish()