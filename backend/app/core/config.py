from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_key: str
    word_source: str = "local"  # default to local word list

    class Config:
        env_file = ".env"  # load from .env


# Create an instance of the Settings class to be used elsewhere
settings = Settings()
