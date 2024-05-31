from typing import List
from fastapi import FastAPI
import app.schema as schema

app = FastAPI()


@app.get("/")
async def get_one() -> schema.Movie:
    return schema.Movie(title='Dune: Part Two', year=2024)

@app.get("/2", response_model=schema.Movie)
async def get_two():
    return { "title": 'Dune: Part One', "year": 2021 }

# TODO: fun returning several movies
@app.get("/all", response_model=List[schema.Movie])
async def get_all():
    return [
         schema.Movie(title='Dune: Part Two', year=2024),
          { "title": 'Dune: Part One', "year": 2021 },
    ]

# TODO: fun receiving a Movie
@app.post("/")
async def add(movie: schema.Movie):
    return True