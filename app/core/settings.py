from pathlib import Path
from typing import List

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # CORS
    allowed_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:3002",
        "http://localhost:3003",
        "http://localhost:3004",
        "http://localhost:3005",
        "https://localhost:3000",
        "http://localhost:8080",
        "https://localhost:8080",
        "https://localhost:3001",
        "https://localhost:3002",
        "https://localhost:3003",
        "https://localhost:3004",
        "https://localhost:3005",
    ]

    DB_USER: str = Field(..., alias="DB_USER")
    DB_PASSWORD: str = Field(..., alias="DB_PASSWORD")
    DB_NAME: str = Field(..., alias="DB_NAME")
    DB_HOST: str = Field(..., alias="DB_HOST")
    DB_PORT: int = Field(..., alias="DB_PORT")

    DATABASE_POOL_SIZE: int = Field(default=20, alias="POOL_SIZE")
    DATABASE_POOL_TIMEOUT: int = Field(default=30, alias="POOL_TIMEOUT")
    DATABASE_POOL_RECYCLE: int = Field(default=3600, alias="POOL_RECYCLE")

    DEBUG: bool = Field(..., alias="DEBUG")

    PROJECT_NAME: str = "Collection Point Payment Gateway"
    PROJECT_VERSION: str = Field(default="V1", alias="PROJECT_VERSION")
    API_V1_PREFIX: str = "/api/v1"
    LOG_LEVEL: str = "INFO"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, alias="ACCESS_TOKEN_EXPIRE_MINUTES")


    @computed_field
    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"



settings = Settings()
