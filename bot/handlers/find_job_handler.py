#######################################
# Обработчик команды для поиска работы #
#######################################
import os
import uuid

import requests

from aiogram import Bot
from aiogram import Router, F
from aiogram import types, html
from aiogram.client import bot
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import ReplyKeyboardRemove

from bot.utils.helpers import FormToCreateResume


from bot.services.repository import ResumeRepository

from bot.db.database import session
from bot.config import config_variables

from bot.utils.keyboards import (
    LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER
)

find_job_router = Router()

# Временное хранилище, позже узнаю как с ним
storage_dict = {}

# Объект класса ResumeRepository
resume_repository = ResumeRepository(session=session)

bot_find_job = Bot(token=config_variables.TOKEN, parse_mode=ParseMode.HTML)


@find_job_router.message(F.text == "🔙 НАЗАД")
async def process_back_to_start(message: types.Message):
    await message.answer(
        "BACK",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER,
            resize_keyboard=True
        )
    )


@find_job_router.message(F.text == "4️⃣ Создать резюме")
async def process_create_resume(message: types.Message, state: FSMContext):
    """
     Обрабатывает запрос на создание резюме.

     Parameters:
         message (types.Message): Сообщение пользователя.
         state (FSMContext): Контекст состояния пользовательского диалога.
     """
    await state.set_state(FormToCreateResume.entering_name)
    await message.answer(
        "📓 Имя Фамилия: ",
        reply_markup=ReplyKeyboardRemove()
    )
    storage_dict["user_id"] = message.from_user.id


@find_job_router.message(FormToCreateResume.entering_name)
async def process_name(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод имени и фамилии при создании резюме.

    Parameters:
        message (types.Message): Сообщение пользователя с введенным именем и фамилией.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(entering_name=message.text)
    await state.set_state(FormToCreateResume.skills)
    await message.answer(
        f"👩‍🏭 {html.quote(message.text)}, твои навыки: "
    )
    storage_dict["entering_name"] = message.text


@find_job_router.message(FormToCreateResume.skills)
async def process_skills(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод навыков при создании резюме.

    Parameters:
        message (types.Message): Сообщение пользователя с введенными навыками.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(skills=message.text)
    await state.set_state(FormToCreateResume.experience)
    await message.answer(
        "💚 Опыт: "
    )
    storage_dict["skills"] = message.text


@find_job_router.message(FormToCreateResume.experience)
async def process_experience(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод опыта при создании резюме.

    Parameters:
        message (types.Message): Сообщение пользователя с введенным опытом.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(experience=message.text)
    await state.set_state(FormToCreateResume.education)
    await message.answer(
        "🧧 Образование: "
    )
    storage_dict["experience"] = message.text


@find_job_router.message(FormToCreateResume.education)
async def process_education(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод образования при создании резюме.

    Parameters:
        message (types.Message): Сообщение пользователя с введенным образованием.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(education=message.text)
    await state.set_state(FormToCreateResume.image_path)
    await message.answer(
        "⬜ Изображение: "
    )
    storage_dict["education"] = message.text


@find_job_router.message(FormToCreateResume.image_path)
async def process_image_path(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    file_id = photo.file_id

    await state.update_data(image_path=file_id)
    storage_dict["image_path"] = file_id
    await message.answer_photo(
        photo=file_id,
        caption=f"""
                Резюме:\n\t\n\t
                Имя: {storage_dict["entering_name"]},\n\t\n\t
                Навыки: {storage_dict["skills"]},\n\t\n\t
                Опыт: {storage_dict["experience"]},\n\t\n\t
                Образование: {storage_dict["education"]},\n\t\n\t
                """,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_START_HANDLER,
            resize_keyboard=True
        )

    )

    # Создаем резюме на основе полученных данных
    try:
        await resume_repository.create_resume(
            user_id=storage_dict["user_id"],
            name=storage_dict["entering_name"],
            skills=storage_dict["skills"],
            experience=storage_dict["experience"],
            education=storage_dict["education"],
            image_path=storage_dict["image_path"]
        )
        await state.clear()
        storage_dict.clear()
    except Exception as ex:
        print(f"Произошла ошибка при создании резюме: {ex}")





