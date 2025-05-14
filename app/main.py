# app/main.py

from fastapi import FastAPI
from app.api.routes import router
# from app.services.word_service import get_word_of_the_day, get_translation_from_api

# create the instance of fastapi app
app = FastAPI()

# the base path
@app.get("/")
def root():
    return {"message": "Welcome to the Spanish Word API!"}

# word of the day endpoint
# @app.get("/word_of_the_day")
# def word_of_the_day():
#     """
#     Get the word of the day.
#     """
#     return get_word_of_the_day()

# include the routes
app.include_router(router)