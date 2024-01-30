#######################################
# Вспомогательные функции и утилиты.  #
#######################################
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup


# Определение состояний
class MyStates(StatesGroup):
    choice = State()