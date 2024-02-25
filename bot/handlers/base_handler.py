from aiogram import (
    Router
)

from bot.handlers.common_handlers import common_router
from bot.handlers.find_job_handler import find_job_router
from bot.handlers.post_job_handler import post_job_router
from bot.handlers.start_handler import start_router
from bot.handlers.display_resumes import display_resume_router
from bot.handlers.display_vacancies import display_vacancy_router


base_router = Router()

base_router.include_routers(
    start_router,
    find_job_router,
    post_job_router,
    display_resume_router,
    display_vacancy_router,
    common_router,
)