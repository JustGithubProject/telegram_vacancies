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
    """Handler to display whole vacancies"""
    vacancies_list = await vacancy_repository.list_vacancies()
    vacancies_list = list(vacancies_list)
    for item in vacancies_list:
        await message.answer_photo(
            photo=item.image_path,
            caption=(
                f"""
                Вакансия:
                Имя компании: {item.company_name},
                Описание: {item.description},
                Местоположение: {item.location},
                Зарплата: {item.salary},
                Контакты: {item.contacts},
                """
            )
        )




