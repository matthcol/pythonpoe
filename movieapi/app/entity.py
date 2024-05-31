from sqlalchemy import Column, Integer, String

from app.database import Base

class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=300), nullable=False, )
    year = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=True)
    poster_uri = Column(String(length=300), nullable=True)