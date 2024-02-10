from sqlalchemy import (
    Column,
    Integer,
    String,
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