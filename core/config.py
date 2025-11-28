import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/fastapi_db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")

settings = Settings()