import random
import requests
from app.core.config import settings

BASE_URL = "https://www.dictionaryapi.com/api/v3/references/spanish/json/"

# list of spanish words (if local is chosen) 
local_words = [
    {"spanish": "hola", "english": "hello"},
    {"spanish": "gracias", "english": "thank you"},
    {"spanish": "amor", "english": "love"},
    {"spanish": "libro", "english": "book"},
    {"spanish": "comida", "english": "food"},
    {"spanish": "familia", "english": "family"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "feliz", "english": "happy"},
    {"spanish": "mañana", "english": "morning"},
    {"spanish": "noche", "english": "night"},
]

def get_word_of_the_day(word: str):
    """
    Get the translation from API or local based on .env setting.
    """
    if settings.word_source == "local":
        return random.choice(local_words)
    elif settings.word_source == "api":
        return get_translation_from_api(word)
    else:
        raise NotImplementedError("Invalid word source in .env file. Choose 'local' or 'api'.")
   
def get_translation_from_api(word: str):
    """
    Get the translation of a word from the API.
    """
    url = f"{BASE_URL}{word}?key={settings.api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if not data or not isinstance(data, list) or not isinstance(data[0], dict):
            raise ValueError("Unexpected API response structure")

        first_entry = data[0]

        word_id = first_entry.get("meta", {}).get("id", "")
        definitions = first_entry.get("shortdef", [])

        if not definitions:
            raise ValueError("No definitions found")
        
        return {
            "word":word_id,
            "meaning": definitions[0]
        }
    

    else:
        raise Exception(f"API request failed with status code {response.status_code}")
    