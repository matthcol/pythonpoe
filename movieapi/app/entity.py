from sqlalchemy import Column, Integer, String

class Movie:
    __tablename__ = 'movie'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(length=300), nullable=False, )
    year = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=True)