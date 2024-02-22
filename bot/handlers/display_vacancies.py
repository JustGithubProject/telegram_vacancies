from aiogram import (
    F,
    types,
    Router
)

from bot.services.repository import VacancyRepository

from bot.db.database import session

# Router that will contain on handler to send list of vacancies to user
display_vacancy_router = Router()

# Repository to get list of vacancies
vacancy_repository = VacancyRepository(session=session)


@display_vacancy_router.message(F.text == "3️⃣ Смотреть вакансии")
async def display_vacancy_process(message: types.Message):
    pass




