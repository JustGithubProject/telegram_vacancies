from sqlalchemy import select

from bot.db.models import Resume


class BaseRepository:
    def __init__(self, session):
        self.session = session


class ResumeRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session)

    async def create_resume(
        self,
        user_id: int,
        name: str,
        skills: str,
        experience: str,
        education: str
    ):
        new_resume = Resume(
            user_id=user_id,
            name=name,
            skills=skills,
            experience=experience,
            education=education
        )
        self.session.add(new_resume)
        await self.session.commit()
        return new_resume

    async def get_resume_by_id(self, resume_id: int):
        result = await self.session.execute(select(Resume).filter(Resume.id == resume_id))
        resume = result.scalars().first()
        return resume


    async def delete_resume(self):
        pass

    async def list_resumes(self):
        pass
