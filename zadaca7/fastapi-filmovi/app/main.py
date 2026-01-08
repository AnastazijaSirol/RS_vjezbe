from fastapi import FastAPI
from app.routers import filmovi

app = FastAPI(title="Filmovi API")

app.include_router(filmovi.router)
