from aiogram import (
    types,
    Router,
    F
)

from services.repository import ResumeRepository

from db.database import session


display_resume_router = Router()

resume_repository = ResumeRepository(session=session)


@display_resume_router.message(F.text == "3️⃣ Смотреть резюме")
async def display_resume_process(message: types.Message):
    """Handler to display whole resumes"""
    resumes_list = await resume_repository.list_resumes()
    resumes_list = list(resumes_list)
    for item in resumes_list:
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

