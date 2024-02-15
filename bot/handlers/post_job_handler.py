###############################################################
# Обработчик команды для размещения вакансии работодателями.   #
###############################################################

from aiogram import (
    Router,
    F,
    types
)
from aiogram.fsm.context import FSMContext

from aiogram.types import ReplyKeyboardRemove


from bot.utils.helpers import FormToCreateVacancy
from bot.services.repository import VacancyRepository
from bot.db.database import session

post_job_router = Router()

storage_dict = {}

# Объект класса VacancyRepository
vacancy_repository = VacancyRepository(session=session)


@post_job_router.message(F.text == "Создать вакансию")
async def process_create_vacancy(message: types.Message, state: FSMContext):
    """
    Обрабатывает запрос на создание новой вакансии.

    Parameters:
        message (types.Message): Сообщение пользователя с запросом на создание вакансии.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.set_state(FormToCreateVacancy.company_name)
    await message.answer(
        "Название компании: ",
        reply_markup=ReplyKeyboardRemove()
    )


@post_job_router.message(FormToCreateVacancy.company_name)
async def process_company_name(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод названия компании при создании вакансии.

    Parameters:
        message (types.Message): Сообщение пользователя с введенным названием компании.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(company_name=message.text)
    await state.set_state(FormToCreateVacancy.description)
    await message.answer(
        "Описание: "
    )
    storage_dict["company_name"] = message.text


@post_job_router.message(FormToCreateVacancy.description)
async def process_description(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод описания вакансии при создании вакансии.

    Parameters:
        message (types.Message): Сообщение пользователя с введенным описанием вакансии.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(description=message.text)
    await state.set_state(FormToCreateVacancy.location)
    await message.answer(
        "Местоположение: "
    )
    storage_dict["description"] = message.text


@post_job_router.message(FormToCreateVacancy.location)
async def process_location(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод местоположения вакансии при создании вакансии.

    Parameters:
        message (types.Message): Сообщение пользователя с введенным местоположением вакансии.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(location=message.text)
    await state.set_state(FormToCreateVacancy.salary)
    await message.answer(
        "Зарплата: "
    )
    storage_dict["location"] = message.text


@post_job_router.message(FormToCreateVacancy.salary)
async def process_salary(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод зарплаты для вакансии при создании вакансии.

    Parameters:
        message (types.Message): Сообщение пользователя с введенной зарплатой для вакансии.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(salary=message.text)
    await state.set_state(FormToCreateVacancy.contacts)
    await message.answer(
        "Контакты: "
    )
    storage_dict["salary"] = message.text


@post_job_router.message(FormToCreateVacancy.contacts)
async def process_contacts(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод контактов для вакансии при создании вакансии

    Parameters:
        message (types.Message): Сообщение пользователя с введенной зарплатой для вакансии.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(contacts=message.text)
    storage_dict["contacts"] = message.text
    storage_dict["user_id"] = message.from_user.id
    await message.answer(
        f"""
        Вакансия:
        Название компании: {storage_dict["company_name"]},
        Описание: {storage_dict["description"]},
        Местоположение: {storage_dict["location"]},
        Зарплата: {storage_dict["salary"]},
        Контакты: {storage_dict["contacts"]}    
        """
    )
    try:
        await vacancy_repository.create_vacancy(
            user_id=storage_dict["user_id"],
            company_name=storage_dict["company_name"],
            description=storage_dict["description"],
            location=storage_dict["location"],
            salary=storage_dict["salary"],
            contacts=storage_dict["contacts"]
        )
        await state.clear()
        storage_dict.clear()

    except Exception as ex:
        print(f"Error occurred when you was trying to create vacancy: {ex}")






