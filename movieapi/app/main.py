from typing import List
from fastapi import FastAPI, Depends
from app import crud
import app.schema as schema
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from app import database

database.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movie/", response_model=List[schema.Movie])
async def get_all(db: Session = Depends(get_db)):
    return crud.get_all(db)

# @app.get("/")
# async def get_one() -> schema.Movie:
#     return schema.Movie(title='Dune: Part Two', year=2024)

# @app.get("/2", response_model=schema.Movie)
# async def get_two():
#     return { "title": 'Dune: Part One', "year": 2021 }

# # TODO: fun returning several movies
# @app.get("/all", response_model=List[schema.Movie])
# async def get_all():
#     return [
#          schema.Movie(title='Dune: Part Two', year=2024),
#           { "title": 'Dune: Part One', "year": 2021 },
#     ]

# # TODO: fun receiving a Movie
# @app.post("/")
# async def add(movie: schema.Movie):
#     return True