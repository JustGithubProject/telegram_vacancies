from typing import List


class BaseRepository:
    def __init__(self, session):
        self.session = session


class UserRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)

    async def create_user(self):
        pass

    async def get_user_by_id(self):
        pass

    async def delete_user(self):
        pass

    async def list_users(self):
        pass




