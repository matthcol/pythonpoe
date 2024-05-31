from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    year: int
    duration: int | None
    poster_uri: str | None

class Movie(MovieCreate):
    id: int

    class Config:
        orm_mode = True