#######################################
# Вспомогательные функции и утилиты.  #
#######################################
from aiogram.fsm.state import State, StatesGroup


# Определение состояний
class FormToCreateResume(StatesGroup):
    choice = State()
    entering_name = State()
