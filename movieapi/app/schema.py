from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    year: int
    duration: int | None

class Movie(MovieCreate):
    id: int