# app/main.py

from fastapi import FastAPI
from app.api.routes import router
from app.services.word_service import get_translation_from_api

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Spanish Word API!"}

# include the routes
app.include_router(router)