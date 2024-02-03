#######################################
# Обработчик команды для поиска работы #
#######################################
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup

keyboard_first = ReplyKeyboardMarkup(resize_keyboard=True)


async def process_create_resume(message: types.Message, state: FSMContext):
    if message.text == "Создать резюме":
        await message.answer("Введите ваше имя: ")
