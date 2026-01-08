from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
from app.models.film import Film

router = APIRouter(prefix="/filmovi", tags=["Filmovi"])

with open("app/data/movies.json", encoding="utf-8") as f:
    raw_movies = json.load(f)

filmovi: List[Film] = [Film(**movie) for movie in raw_movies]

@router.get("/", response_model=List[Film])
def get_all_movies(
    type: Optional[str] = Query(
        None,
        pattern="^(movie|series)$",
        description="Filtriranje po tipu: movie ili series"
    ),
    min_year: Optional[int] = Query(None, description="Minimalna godina izlaska"),
    max_year: Optional[int] = Query(None, description="Maksimalna godina izlaska"),
    min_rating: Optional[float] = Query(None, description="Minimalna ocjena IMDB"),
    max_rating: Optional[float] = Query(None, description="Maksimalna ocjena IMDB")
):
    result = filmovi

    if type:
        result = [f for f in result if f.Type == type]

    if min_year is not None:
        result = [
            f for f in result
            if f.Year.isdigit() and int(f.Year) >= min_year
        ]

    if max_year is not None:
        result = [
            f for f in result
            if f.Year.isdigit() and int(f.Year) <= max_year
        ]

    if min_rating is not None:
        result = [
            f for f in result
            if f.imdbRating not in (None, "N/A") and float(f.imdbRating) >= min_rating
        ]

    if max_rating is not None:
        result = [
            f for f in result
            if f.imdbRating not in (None, "N/A") and float(f.imdbRating) <= max_rating
        ]

    return result


@router.get("/{imdb_id}", response_model=Film)
def get_movie_by_id(imdb_id: str):
    for film in filmovi:
        if film.imdbID == imdb_id:
            return film
    raise HTTPException(
        status_code=404,
        detail="Film s tim imdbID-om ne postoji"
    )


@router.get("/title/{title}", response_model=Film)
def get_movie_by_title(title: str):
    for film in filmovi:
        if film.Title.lower() == title.lower():
            return film
    raise HTTPException(
        status_code=404,
        detail="Film s tim naslovom ne postoji"
    )
