############################################################################################
# Файл с конфигурационными переменными, такими как токен бота, параметры базы данных и т.д #
############################################################################################

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.TOKEN = os.getenv("TOKEN")
        self.DATABASE_URL = os.getenv("DATABASE_URL")


config_variables = Config()
