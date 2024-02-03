#########################################################################
# Общие обработчики, например, обработчик для неопознанных команд.      #
#########################################################################
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

from handlers.find_job_handler import process_create_resume


# Объявляем клавиатуру

keyboard_second = ReplyKeyboardMarkup(resize_keyboard=True)

# Добавляем кнопки на клавиатуру


buttons_second = [

]

# Добавляем кнопки на клавиатуру

keyboard_second.add(*buttons_second)


async def process_choice(message: types.Message, state: FSMContext):
    if message.text == "Я предлагаю работу":
        await message.answer("Вы выбрали: Я предлагаю работу", reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Смотреть резюме"),
                    KeyboardButton(text="Создать вакансию"),
                ]
            ],
            resize_keyboard=True
        )
    )

    elif message.text == "Я ищу работу":
        await message.answer("Вы выбрали: Я ищу работу", reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Смотреть вакансии"),
                    KeyboardButton(text="Создать резюме")
                ]
            ],
            resize_keyboard=True
        )
    )


