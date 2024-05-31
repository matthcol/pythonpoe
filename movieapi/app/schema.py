from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    year: int
    duration: int | None