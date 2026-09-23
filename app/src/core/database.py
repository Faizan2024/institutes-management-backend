from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.core.config import settings

engine = create_engine(url=settings.DATABASE_URL)
LocalSession = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass