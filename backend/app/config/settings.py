from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "Project Atlas API"
    APP_VERSION: str = "0.1.0"
    ENVIRONMENT: str = "development"

    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "atlas"
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()
