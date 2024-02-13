from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

from db.database import Base


class Resume(Base):
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    name = Column(String, nullable=False)
    skills = Column(String)
    experience = Column(String)
    education = Column(String)


class Vacancy(Base):
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    company_name = Column(String, nullable=False)
    description = Column(String)
    location = Column(String)
    salary = Column(Float(precision=2))
    contacts = Column(String)
