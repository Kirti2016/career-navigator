from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    from sqlalchemy import Column, Integer, Text
from app.database import Base

class ResumeParsedData(Base):
    __tablename__ = "resume_parsed_data"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)

