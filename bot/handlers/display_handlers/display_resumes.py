from typing import List

from aiogram import (
    types,
    Router,
    F
)
from aiogram.types import ReplyKeyboardMarkup

from db.models import Resume
from services.repository import ResumeRepository

from db.database import session
from utils.keyboards import LIST_KEYBOARD_BUTTONS_FOR_DISPLAY_RESUME_HANDLER


display_resume_router = Router()

# Creating a repository instance
resume_repository = ResumeRepository(session=session)


# Global variable to keep track of resume index
index = 0


async def send_resume(message: types.Message, resumes_list: List[Resume], index_of_resume: int):
    global index
    if index >= len(resumes_list):
        index = 0
        await message.answer("Больше нет новых резюме. Нажмите next, чтобы начать с начала")

    item = resumes_list[index_of_resume]

    await message.answer_photo(
        photo=item.image_path,
        caption=(
            f"""
              Резюме:
              Имя: {item.name.strip()},
              Навыки: {item.skills.strip()},
              Опыт: {item.experience.strip()},
              Образование: {item.education.strip()}
          """
        )
    )


@display_resume_router.message(F.text == "3️⃣ Смотреть резюме")
async def display_resume_process(message: types.Message):
    """Handler to display whole resumes"""
    resumes_list = await resume_repository.list_resumes()
    resumes_list = list(resumes_list)

    await send_resume(message, resumes_list, index)
    await message.answer(
        "Для просмотра следующего резюме введите 'Next'.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_DISPLAY_RESUME_HANDLER,
            resize_keyboard=True
        )
    )


@display_resume_router.message(F.text == "Next")
async def next_resume(message: types.Message):
    resumes_list = await resume_repository.list_resumes()
    resumes_list = list(resumes_list)
    global index
    index += 1
    await send_resume(message, resumes_list, index)
