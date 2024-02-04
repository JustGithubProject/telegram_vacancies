#########################################################################
# Общие обработчики, например, обработчик для неопознанных команд.      #
#########################################################################
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton
from aiogram.types import ReplyKeyboardMarkup

from handlers.find_job_handler import process_create_resume
from main import first_router


@first_router.message()
async def process_choice(message: types.Message):
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


