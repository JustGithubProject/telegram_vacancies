###################################################################################################################
# Главный файл, запускающий бота. В этом файле будет код для создания и запуска бота, а также обработчиков событий#
###################################################################################################################
import logging
import asyncio
import sys


from aiogram import (
    Bot,
    Dispatcher,
)
from aiogram.enums import ParseMode

from config import config_variables

from handlers.base_handler import base_router


async def main():
    bot = Bot(token=config_variables.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    # Включение обработчиков роутеров для различных типов обработки запросов
    dp.include_router(base_router)

    # Запуск бота с использованием диспетчера
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
asyncio.run(main())