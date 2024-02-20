#########################################################################
# Общие обработчики, например, обработчик для неопознанных команд.      #
#########################################################################
from aiogram import (
    Router,
    types,
    F
)

from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup
)

from bot.services.repository import ResumeRepository
from bot.db.database import session

# router for handlers
common_router = Router()


@common_router.message()
async def process_choice(message: types.Message):
    if message.text == "1️⃣ Я предлагаю работу":
        await message.answer("✅ Вы выбрали: Я предлагаю работу", reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="3️⃣ Смотреть резюме"),
                    KeyboardButton(text="4️⃣ Создать вакансию"),
                ]
            ],
            resize_keyboard=True
        )
    )

    elif message.text == "2️⃣ Я ищу работу":
        await message.answer("✅ Вы выбрали: Я ищу работу", reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="3️⃣ Смотреть вакансии"),
                    KeyboardButton(text="4️⃣ Создать резюме")
                ]
            ],
            resize_keyboard=True
        )
    )


