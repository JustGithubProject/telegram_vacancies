#######################################
# Вспомогательные функции и утилиты.  #
#######################################
from aiogram.fsm.state import State, StatesGroup


# Определение состояний
class FormToCreateResume(StatesGroup):
    entering_name = State()
    skills = State()
    experience = State()
    education = State()
    image_path = State()


class FormToCreateVacancy(StatesGroup):
    company_name = State()
    description = State()
    location = State()
    salary = State()
    contacts = State()
    # ....
