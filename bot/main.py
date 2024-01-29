###################################################################################################################
# Главный файл, запускающий бота. В этом файле будет код для создания и запуска бота, а также обработчиков событий#
###################################################################################################################
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor

from config import config_variables
from handlers.start_handler import send_welcome

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config_variables.TOKEN)

dp = Dispatcher(bot)

dp.register_message_handler(send_welcome, commands=['start'])

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
