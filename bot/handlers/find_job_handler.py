#######################################
# Обработчик команды для поиска работы #
#######################################
from aiogram import Router, F
from aiogram import types, html
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from bot.utils.helpers import FormToCreateResume


from bot.services.repository import ResumeRepository

from bot.db.database import session


find_job_router = Router()

# Временное хранилище, позже узнаю как с ним
storage_dict = {}

# Объект класса ResumeRepository
resume_repository = ResumeRepository(session=session)


@find_job_router.message(F.text == "Создать резюме")
async def process_create_resume(message: types.Message, state: FSMContext):
    """
     Обрабатывает запрос на создание резюме.

     Parameters:
         message (types.Message): Сообщение пользователя.
         state (FSMContext): Контекст состояния пользовательского диалога.
     """
    await state.set_state(FormToCreateResume.entering_name)
    await message.answer(
        "Имя Фамилия: ",
        reply_markup=ReplyKeyboardRemove()
    )
    storage_dict["user_id"] = message.from_user.id


@find_job_router.message(FormToCreateResume.entering_name)
async def process_name(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод имени и фамилии при создании резюме.

    Parameters:
        message (types.Message): Сообщение пользователя с введенным именем и фамилией.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(entering_name=message.text)
    await state.set_state(FormToCreateResume.skills)
    await message.answer(
        f"{html.quote(message.text)}, твои навыки: "
    )
    storage_dict["entering_name"] = message.text


@find_job_router.message(FormToCreateResume.skills)
async def process_skills(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод навыков при создании резюме.

    Parameters:
        message (types.Message): Сообщение пользователя с введенными навыками.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(skills=message.text)
    await state.set_state(FormToCreateResume.experience)
    await message.answer(
        "Опыт: "
    )
    storage_dict["skills"] = message.text


@find_job_router.message(FormToCreateResume.experience)
async def process_experience(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод опыта при создании резюме.

    Parameters:
        message (types.Message): Сообщение пользователя с введенным опытом.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(experience=message.text)
    await state.set_state(FormToCreateResume.education)
    await message.answer(
        "Образование: "
    )
    storage_dict["experience"] = message.text


@find_job_router.message(FormToCreateResume.education)
async def process_education(message: types.Message, state: FSMContext):
    """
    Обрабатывает ввод образования при создании резюме.

    Parameters:
        message (types.Message): Сообщение пользователя с введенным образованием.
        state (FSMContext): Контекст состояния пользовательского диалога.
    """
    await state.update_data(education=message.text)
    storage_dict["education"] = message.text
    await message.answer(
        f"""
        Резюме:
        Имя: {storage_dict['entering_name']}
        Навыки: {storage_dict["skills"]}
        Опыт: {storage_dict["experience"]}
        Образование: {storage_dict["education"]}
        """
    )
    try:
        await resume_repository.create_resume(
            user_id=storage_dict["user_id"],
            name=storage_dict["entering_name"],
            skills=storage_dict["skills"],
            experience=storage_dict["experience"],
            education=storage_dict["education"]
        )
        await state.clear()
        storage_dict.clear()
    except Exception as ex:
        print(f"Error occurred when you was trying to create resume: {ex}")






