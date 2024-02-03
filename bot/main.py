###################################################################################################################
# Главный файл, запускающий бота. В этом файле будет код для создания и запуска бота, а также обработчиков событий#
###################################################################################################################
import logging
import asyncio
import sys


from aiogram import (
    Bot,
    Dispatcher,
    Router
)
from aiogram.enums import ParseMode

from config import config_variables
from handlers.find_job_handler import process_create_resume
from handlers.start_handler import send_welcome
from handlers.common_handlers import process_choice


first_router = Router()


async def main():
    bot = Bot(token=config_variables.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(first_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())