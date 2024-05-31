from sqlalchemy.orm import Session

from app import entity

def save(db: Session):
    pass

def get_all(db: Session):
    return db.query(entity.Movie).all()

def get_by_id(db: Session):
    pass

def get_by_year(db: Session):
    pass

def get_by_title(db: Session):
    pass