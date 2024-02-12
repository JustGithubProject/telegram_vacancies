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

# object of ResumeRepository
resume_repository = ResumeRepository(session=session)

# хранение текущего индекса резюме пользователя
user_resume_index = {}


@common_router.message()
async def process_choice(message: types.Message):
    if message.text == "1️⃣ Я предлагаю работу":
        await message.answer("✅ Вы выбрали: Я предлагаю работу", reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Смотреть резюме"),
                    KeyboardButton(text="Создать вакансию"),
                ]
            ],
            resize_keyboard=True
        )
    )

    elif message.text == "2️⃣ Я ищу работу":
        await message.answer("✅ Вы выбрали: Я ищу работу", reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Смотреть вакансии"),
                    KeyboardButton(text="Создать резюме")
                ]
            ],
            resize_keyboard=True
        )
    )


@common_router.message(F.text == "Смотреть резюме")
async def process_display_resume(message: types.Message):
    # Получаем список резюме
    resumes = await resume_repository.list_resumes()

    user_id = message.from_user.id
    user_resume_index[user_id] = 0
    await display_resume(message, resumes)


async def display_resume(message: types.Message, resumes: list):
    user_id = message.from_user.id
    index = user_resume_index[user_id]
    resume = resumes[index]
    await message.answer(f"Информация о резюме: {resume}")
    await message.answer(
        "Нажмите 'Next' для просмотра следующего резюме",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Next")
                ]
            ],
            resize_keyboard=True
        )
    )


@common_router.message(F.text == "Next")
async def process_next_resume(message: types.Message):
    resumes = await resume_repository.list_resumes()

    user_id = message.from_user.id
    index = user_resume_index[user_id]
    if index >= len(resumes):
        await message.answer("Вы достигли конца списка резюме!")
    else:
        index += 1
        user_resume_index[user_id] = index
        await display_resume(message, resumes=resumes)