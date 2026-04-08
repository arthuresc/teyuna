# Implementar verificação de erros do pydantic e pydantic_settings aqui
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True)
    
    # Configuração de DB SQL
    DATABASE_URL_ASYNC: str = Field("DATABASE_URL_SYNC")
    DATABASE_URL_SYNC: str = Field("DATABASE_URL_ASYNC")
    DB_USER: str = Field("DB_USER")
    DB_PASS: str = Field("DB_PASS")
    DB_NAME: str = Field("DB_NAME")
    
    # Configuração de ambiente
    ENVIROMENT: Optional[str] = Field(default="development", alias='ENVIROMENT')
    DEBUG: bool = Field(default=False, alias='DEBUG')
    
    
    # SECRET_KEY: str = Field("DATABASE_URL_SYNC")
    
settings = Settings()