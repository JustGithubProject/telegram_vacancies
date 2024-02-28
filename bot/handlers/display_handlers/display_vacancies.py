from typing import List

from aiogram import (
    F,
    types,
    Router
)
from aiogram.types import ReplyKeyboardMarkup

from db.models import Vacancy
from services.repository import VacancyRepository

from db.database import session

# Router that will contain on handler to send list of vacancies to user
from utils.keyboards import (
    LIST_KEYBOARD_BUTTONS_FOR_DISPLAY_RESUME_HANDLER,
    LIST_KEYBOARD_BUTTONS_FOR_DISPLAY_VACANCY_HANDLER
)
display_vacancy_router = Router()

# Repository to get list of vacancies
vacancy_repository = VacancyRepository(session=session)

index = 0


async def send_vacancy(message: types.Message, vacancies_list: List[Vacancy], index_of_vacancy: int):
    global index
    if index >= len(vacancies_list):
        index = 0
        await message.answer("Больше нет новых вакансий")

    item = vacancies_list[index_of_vacancy]
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


@display_vacancy_router.message(F.text == "3️⃣ Смотреть вакансии")
async def display_vacancy_process(message: types.Message):
    """Handler to display whole vacancies"""
    vacancies_list = await vacancy_repository.list_vacancies()
    vacancies_list = list(vacancies_list)

    await send_vacancy(message, vacancies_list, index)
    await message.answer(
        "Для просмотра следующего резюме введите 'NEXT'.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=LIST_KEYBOARD_BUTTONS_FOR_DISPLAY_VACANCY_HANDLER,
            resize_keyboard=True
        )
    )


@display_vacancy_router.message(F.text == "NEXT")
async def next_vacancy(message: types.Message):
    vacancies_list = await vacancy_repository.list_vacancies()
    vacancies_list = list(vacancies_list)
    global index
    index += 1
    await send_vacancy(message, vacancies_list, index)




