from pydantic import BaseModel
from typing import List, Optional, Literal

class Film(BaseModel):
    Title: str
    Year: str
    Rated: str
    Runtime: str
    Genre: str
    Language: str
    Country: str
    Actors: str
    Plot: str
    Writer: str

    Images: List[str] = []
    Type: Literal["movie", "series"]

    imdbID: Optional[str] = None
    imdbRating: Optional[str] = None
    imdbVotes: Optional[str] = None
