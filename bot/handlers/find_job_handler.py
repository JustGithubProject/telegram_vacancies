#######################################
# Обработчик команды для поиска работы #
#######################################
from aiogram import types, html
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from main import first_router
from utils.helpers import FormToCreateResume


@first_router.message()
async def process_create_resume(message: types.Message, state: FSMContext):
    if message.text == "Создать резюме":
        await state.set_state(FormToCreateResume.entering_name)
        await message.answer(
            "Введите ваше имя: ",
            reply_markup=ReplyKeyboardRemove()
        )


@first_router.message(FormToCreateResume.entering_name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(entering_name=message.text)
    await state.set_state(FormToCreateResume.skills)
    await message.answer(
        f"{html.quote(message.text)}, твои навыки: "
    )


@first_router.message(FormToCreateResume.skills)
async def process_skills(message: types.Message, state: FSMContext):
    await state.update_data(skills=message.text)
    await state.set_state(FormToCreateResume.experience)
    await message.answer(
        "Опыт: "
    )


@first_router.message(FormToCreateResume.experience)
async def process_experience(message: types.Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await state.set_state(FormToCreateResume.education)
    await message.answer(
        "Образование: "
    )




