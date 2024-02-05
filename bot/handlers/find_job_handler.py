#######################################
# Обработчик команды для поиска работы #
#######################################
from aiogram import Router, F
from aiogram import types, html
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from utils.helpers import FormToCreateResume


find_job_handler_router = Router()


@find_job_handler_router.message(F.text == "Создать резюме")
async def process_create_resume(message: types.Message, state: FSMContext):
    await state.set_state(FormToCreateResume.entering_name)
    await message.answer(
        "Введите ваше имя: ",
        reply_markup=ReplyKeyboardRemove()
    )


@find_job_handler_router.message(FormToCreateResume.entering_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(entering_name=message.text)
    await state.set_state(FormToCreateResume.skills)
    await message.answer(
        f"{html.quote(message.text)}, твои навыки: "
    )


@find_job_handler_router.message(FormToCreateResume.skills)
async def process_skills(message: types.Message, state: FSMContext):
    await state.update_data(skills=message.text)
    await state.set_state(FormToCreateResume.experience)
    await message.answer(
        "Опыт: "
    )


@find_job_handler_router.message(FormToCreateResume.experience)
async def process_experience(message: types.Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await state.set_state(FormToCreateResume.education)
    await message.answer(
        "Образование: "
    )




