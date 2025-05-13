from fastapi import APIRouter
from app.services.word_service import get_word_of_the_day

router = APIRouter()

@router.get("/translate/{word}")
def translate_word(word: str):
    return get_word_of_the_day(word)
