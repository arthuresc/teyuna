from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

from core.config import settings
  
  
# class Settings(BaseSettings):
  
#   DATABASE_URL_SYNC: str = Field("DATABASE_URL_SYNC")
#   DATABASE_URL_ASYNC: str = Field("DATABASE_URL_ASYNC")
#   DB_USER: str = Field("DB_USER")
#   DB_PASS: str = Field("DB_PASS")
#   DB_NAME: str = Field("DB_NAME")
  
#   model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True)


# settings = Settings()

def get_values():
  print(settings.ENVIROMENT)
# TeSte
get_values()