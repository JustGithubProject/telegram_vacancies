from typing import List

from aiogram import Dispatcher
from aiogram import (
    types,
    Router,
    F
)
from aiogram.utils.formatting import Text

from db.models import Resume
from services.repository import ResumeRepository

from db.database import session


display_resume_router = Router()

resume_repository = ResumeRepository(session=session)

index = 0


async def send_resume(message: types.Message, resumes_list: List[Resume], index_of_resume: int):
    if index >= len(resumes_list):
        await message.answer("Больше нет новых резюме")

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
    await message.answer("Для просмотра следующего резюме введите 'Next'.")


@display_resume_router.message(F.text == "Next")
async def next_resume(message: types.Message):
    resumes_list = await resume_repository.list_resumes()
    resumes_list = list(resumes_list)
    global index
    index += 1
    await send_resume(message, resumes_list, index)
