from sqlalchemy import select

from bot.db.models import (
    Resume,
    Vacancy
)


class BaseRepository:
    """Base class for repository implementations"""
    def __init__(self, session):
        self.session = session


class ResumeRepository(BaseRepository):
    """Repository for managing Resume objects in the database"""
    def __init__(self, session):
        super().__init__(session)

    async def create_resume(
        self,
        user_id: int,
        name: str,
        skills: str,
        experience: str,
        education: str,
        image_path: str
    ):
        new_resume = Resume(
            user_id=user_id,
            name=name,
            skills=skills,
            experience=experience,
            education=education,
            image_path=image_path
        )
        self.session.add(new_resume)
        await self.session.commit()
        return new_resume

    async def get_resume_by_id(self, resume_id: int):
        result = await self.session.execute(select(Resume).filter(Resume.id == resume_id))
        resume = result.scalars().first()
        return resume

    async def delete_resume(self, resume_id: int):
        resume = await self.get_resume_by_id(resume_id)
        if not resume:
            raise ValueError(f"Resume with ID {resume_id} does not exist")

        await self.session.delete(resume)
        await self.session.commit()

    async def list_resumes(self):
        result = await self.session.execute(select(Resume))
        resumes = result.scalars().all()
        return resumes


class VacancyRepository(BaseRepository):
    """Repository for managing Vacancy objects in database"""
    def __init__(self, session):
        super().__init__(session)

    async def create_vacancy(
        self,
        user_id: int,
        company_name: str,
        description: str,
        location: str,
        salary: float,
        contacts: str,
        image_path: str
    ):
        new_vacancy = Vacancy(
            user_id=user_id,
            company_name=company_name,
            description=description,
            location=location,
            salary=salary,
            contacts=contacts,
            image_path=image_path
        )

        self.session.add(new_vacancy)
        await self.session.commit()
        return new_vacancy

    async def get_vacancy_by_id(
        self,
        vacancy_id: int
    ):
        result = await self.session.execute(select(Vacancy).filter(Vacancy.id == vacancy_id))
        vacancy = result.scalars().first()
        return vacancy

    async def delete_vacancy(
        self,
        vacancy_id: int
    ):
        vacancy = await self.get_vacancy_by_id(vacancy_id)
        if not vacancy:
            raise ValueError(f"Vacancy with {vacancy_id} doesn't exist")

        await self.session.delete(vacancy)
        await self.session.commit()

    async def list_vacancies(self):
        result = await self.session.execute(select(Vacancy))
        vacancies = result.scalars().all()
        return vacancies
