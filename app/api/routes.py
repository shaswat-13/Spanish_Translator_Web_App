from fastapi import APIRouter
from app.services.word_service import get_word_of_the_day

router = APIRouter()

@router.get("/translate/{sp_word}")
def translate_word(sp_word: str):
    return get_word_of_the_day(sp_word)
