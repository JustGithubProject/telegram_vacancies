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

from utils.helpers import FormToCreateVacancy

post_job_router = Router()

storage_dict = {}


@post_job_router.message(F.text == "Создать вакансию")
async def process_create_vacancy(message: types.Message, state: FSMContext):
    await state.set_state(FormToCreateVacancy.company_name)
    await message.answer(
        "Название компании: ",
        reply_markup=ReplyKeyboardRemove()
    )


@post_job_router.message(FormToCreateVacancy.company_name)
async def process_company_name(message: types.Message, state: FSMContext):
    await state.update_data(company_name=message.text)
    await state.set_state(FormToCreateVacancy.description)
    await message.answer(
        "Описание: "
    )

