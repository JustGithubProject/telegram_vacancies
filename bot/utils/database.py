##########################################################################################
#  Модуль для работы с базой данных, например, сохранение данных о вакансиях и резюме    #
###########################################################################################
from sqlalchemy import (
    create_engine,
)

from sqlalchemy.orm import sessionmaker

from config import config_variables
from sqlalchemy.orm import declarative_base

Base = declarative_base()


engine = create_engine(config_variables.DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)








