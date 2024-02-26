##########################################################################################
#  Модуль для работы с базой данных, например, сохранение данных о вакансиях и резюме    #
###########################################################################################

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


session = async_session()









