# app/db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.database import Base, engine

def init_db():
    Base.metadata.create_all(bind=engine)


DB_URL = os.getenv("DB_URL", "sqlite:///./career_nav.db")

# For SQLite, check_same_thread must be False for multithreading
engine = create_engine(
    DB_URL, connect_args={"check_same_thread": False} if DB_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from app import rename  # noqa: F401 (ensure models are imported)
    Base.metadata.create_all(bind=engine)
