from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

from db.database import Base


class Resume(Base):
    """Model that represents resume table in database"""
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    name = Column(String, nullable=False)
    skills = Column(String)
    experience = Column(String)
    education = Column(String)
    image_path = Column(String)


class Vacancy(Base):
    """Model that represents vacancy table in database"""
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    company_name = Column(String, nullable=False)
    description = Column(String)
    location = Column(String)
    salary = Column(Float(precision=2))
    contacts = Column(String)
    image_path = Column(String)
