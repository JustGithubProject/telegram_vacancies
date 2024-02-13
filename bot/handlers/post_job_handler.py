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


post_job_router = Router()

storage_dict = {}


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



