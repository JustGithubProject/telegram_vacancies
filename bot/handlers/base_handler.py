from aiogram import (
    Router
)

from handlers.main_handlers.common_handlers import common_router
from handlers.main_handlers.find_job_handler import find_job_router
from handlers.main_handlers.post_job_handler import post_job_router
from handlers.command_handlers.start_handler import start_router
from handlers.display_handlers.display_resumes import display_resume_router
from handlers.display_handlers.display_vacancies import display_vacancy_router

# Базовый роутер, который подключает остальные роутеры
base_router = Router()

base_router.include_routers(
    start_router,
    find_job_router,
    post_job_router,
    display_resume_router,
    display_vacancy_router,
    common_router,
)