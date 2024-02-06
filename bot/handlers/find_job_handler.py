#######################################
# Обработчик команды для поиска работы #
#######################################
from aiogram import Router, F
from aiogram import types, html
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from utils.helpers import FormToCreateResume


find_job_router = Router()

storage_dict = {}


@find_job_router.message(F.text == "Создать резюме")
async def process_create_resume(message: types.Message, state: FSMContext):
    print("Working")
    await state.set_state(FormToCreateResume.entering_name)
    await message.answer(
        "Введите ваше имя: ",
        reply_markup=ReplyKeyboardRemove()
    )


@find_job_router.message(FormToCreateResume.entering_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(entering_name=message.text)
    await state.set_state(FormToCreateResume.skills)
    await message.answer(
        f"{html.quote(message.text)}, твои навыки: "
    )
    storage_dict["entering_name"] = message.text


@find_job_router.message(FormToCreateResume.skills)
async def process_skills(message: types.Message, state: FSMContext):
    await state.update_data(skills=message.text)
    await state.set_state(FormToCreateResume.experience)
    await message.answer(
        "Опыт: "
    )
    storage_dict["skills"] = message.text


@find_job_router.message(FormToCreateResume.experience)
async def process_experience(message: types.Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await state.set_state(FormToCreateResume.education)
    await message.answer(
        "Образование: "
    )
    storage_dict["experience"] = message.text


@find_job_router.message(FormToCreateResume.education)
async def process_education(message: types.Message, state: FSMContext):
    await state.update_data(education=message.text)
    storage_dict["education"] = message.text
    await message.answer(
        f"""
            
            Имя: {storage_dict['entering_name']}
            Навыки: {storage_dict["skills"]}
            Опыт: {storage_dict["experience"]}
            Образование: {storage_dict["education"]}
            
        """
    )




