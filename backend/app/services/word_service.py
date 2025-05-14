from datetime import datetime
import json
import random
import requests
from app.core.config import settings
from app.core.logging import logger

# Base URL for the Spanish dictionary API
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

# Load the file with 15k spanish words
with open("data/spanish_words.txt", "r", encoding="utf-8") as f:
    spanish_word_list = [line.strip() for line in f if line.strip()]


# get the word of the day and return its translation
def get_word_of_the_day():
    # Use today's date to seed the random generator
    today_str = datetime.now().strftime("%Y-%m-%d")
    random.seed(today_str + "5")  # Ensures same word throughout the day

    if settings.word_source == "local":
        return random.choice(local_words)

    elif settings.word_source == "api":
        random_word = random.choice(spanish_word_list)
        return get_translation_from_api(random_word)

    else:
        raise NotImplementedError(
            "Invalid word source in .env file. Choose 'local' or 'api'."
        )


# get the translation of a word from the API
def get_translation_from_api(spanish_word):
    def fetch_translation(word):
        """
        Helper function to fetch translation data from Merriam-Webster API.
        """
        url = f"{BASE_URL}{spanish_word}?key={settings.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed for {word}: {e}")
            return None

    try:
        data = fetch_translation(spanish_word)
        if data is None:
            raise ValueError("No response data")

        logger.debug(f"API response was:\n{json.dumps(data, indent=2)}")

        # Case 1: No direct match — it's just a list of suggestions
        if isinstance(data, list) and data and isinstance(data[0], str):
            logger.info(f"No direct match for'{spanish_word}'. Suggestions: {data[:5]}")
            suggestion = data[0]
            suggestion_data = fetch_translation(suggestion)

            if (
                suggestion_data
                and isinstance(suggestion_data, list)
                and "shortdef" in suggestion_data[0]
            ):
                return {
                    "spanish": spanish_word,
                    "english": suggestion_data[0]["shortdef"][0],
                    "suggested": suggestion,
                }
            else:
                return {
                    "spanish": spanish_word,
                    "english": "(no accurate match found)",
                    "suggested": suggestion,
                }

        # Case 2: Direct match
        if isinstance(data, list) and "shortdef" in data[0]:
            return {"spanish": spanish_word, "english": data[0]["shortdef"][0]}

        # Case 3: Unexpected structure
        logger.warning(f"Unexpected API response structure for{spanish_word}")
        return {"spanish": spanish_word, "english": "(no translation found)"}

    except Exception as e:
        logger.error(f"Error parsing API response for {spanish_word}: {e}")
        return {"spanish": spanish_word, "english": "(no translation found)"}


def get_random_word():
    """
    Get a random word from the local list.
    """
    random_word = random.choice(spanish_word_list)
    return get_translation_from_api(random_word)
