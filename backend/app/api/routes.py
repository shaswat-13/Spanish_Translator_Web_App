from fastapi import APIRouter
from app.services.word_service import (
    get_word_of_the_day,
    get_translation_from_api,
    get_random_word,
)

router = APIRouter()


# translate endpoint
@router.get("/translate/{sp_word}")
def translate_word(sp_word: str):
    return get_translation_from_api(sp_word)


# word of the day endpoint
@router.get("/word_of_the_day")
def word_of_the_day():
    return get_word_of_the_day()


# random word endpoint
@router.get("/random")
def random_word():
    return get_random_word()
