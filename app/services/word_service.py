from datetime import datetime
import json
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

# Load the file with 50k spanish words
with open("data/spanish_words.txt", "r", encoding="utf-8") as f:
    spanish_word_list = [line.strip() for line in f if line.strip()]


def get_word_of_the_day():
    # Use today's date to seed the random generator
    today_str = datetime.now().strftime("%Y-%m-%d")
    random.seed(today_str)  # Ensures same word throughout the day

    if settings.word_source == "local":
        return random.choice(local_words)

    elif settings.word_source == "api":
        random_word = random.choice(spanish_word_list)
        return get_translation_from_api(random_word)
    
    else:
        raise NotImplementedError("Invalid word source in .env file. Choose 'local' or 'api'.")

   
def get_translation_from_api(spanish_word):
    url = f"{BASE_URL}{spanish_word}?key={settings.api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"API request failed with status code {response.status_code}")
        return {
            "spanish": spanish_word,
            "english": "(translation unavailable)"
        }
    
    try:
        data = response.json()
        print("DEBUG: API response was:", json.dumps(data, indent=2))

        # Case 1: Word not found, API returns list of suggestion strings
        if isinstance(data, list) and data and isinstance(data[0], str):
            print(f"No direct match for '{spanish_word}'. Suggestions: {data[:5]}")
            return {
                "spanish": spanish_word,
                "english": "(no translation found)"
            }

        # Case 2: Valid translation response with 'shortdef'
        if isinstance(data, list) and "shortdef" in data[0]:
            translation = data[0]["shortdef"][0]
            return {
                "spanish": spanish_word,
                "english": translation
            }

        # Case 3: Unexpected structure
        print("Unexpected API response structure")
        return {
            "spanish": spanish_word,
            "english": "(no translation found)"
        }

    except Exception as e:
        print(f"Error parsing API response: {e}")
        return {
            "spanish": spanish_word,
            "english": "(no translation found)"
        }

def get_random_word():
    """
    Get a random word from the local list.
    """
    random_word = random.choice(spanish_word_list)
    return get_translation_from_api(random_word)