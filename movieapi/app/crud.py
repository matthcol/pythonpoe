from sqlalchemy import func
from sqlalchemy.orm import Session

from app import entity, schema

def save(db: Session, movie_create: schema.MovieCreate):
    movie_db = entity.Movie(**movie_create.dict())
    db.add(movie_db)
    db.commit()
    db.refresh(movie_db)
    return movie_db

def get_all(db: Session):
    return db.query(entity.Movie).all()

def get_by_id(db: Session, movie_id: int):
    return db.query(entity.Movie).get(movie_id)

def get_by_year(db: Session, year: int):
    return db.query(entity.Movie).filter(entity.Movie.year == year)

def get_by_title(db: Session, title: str):
    return db.query(entity.Movie).filter(func.lower(entity.Movie.title).contains(func.lower(title))).all()