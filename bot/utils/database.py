##########################################################################################
#  Модуль для работы с базой данных, например, сохранение данных о вакансиях и резюме    #
###########################################################################################
import asyncio

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

from config import config_variables


# Асинхронный движок SQLAlchemy
engine = create_async_engine(config_variables.DATABASE_URL, echo=True)

# Базовый класс для определения моделей
Base = declarative_base()

# Асинхронная сессия
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# Создаем таблицы в базе данных
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)








