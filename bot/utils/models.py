from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
)

from utils.database import Base


class Resume(Base):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    name = Column(String)
    skills = Column(Text)
    experience = Column(Text)
    education = Column(Text)