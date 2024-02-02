###################################################################################################################
# Главный файл, запускающий бота. В этом файле будет код для создания и запуска бота, а также обработчиков событий#
###################################################################################################################
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor

from config import config_variables
from handlers.find_job_handler import process_create_resume
from handlers.start_handler import send_welcome
from handlers.common_handlers import process_choice

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config_variables.TOKEN)

dp = Dispatcher(bot)

dp.register_message_handler(send_welcome, commands=['start'])
dp.register_message_handler(process_choice, lambda message: message.text in ["Я предлагаю работу", "Я ищу работу"])
dp.register_message_handler(process_create_resume, lambda message: message.text in ["Создать резюме"])

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
