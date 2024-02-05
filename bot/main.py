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
from handlers.start_handler import start_router
from handlers.common_handlers import common_router
from handlers.find_job_handler import find_job_handler_router


async def main():
    bot = Bot(token=config_variables.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(common_router)
    dp.include_router(find_job_handler_router)

    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
asyncio.run(main())