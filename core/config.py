from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL = "postgresql+asyncpg://user:password@db/restaurant_db"
    SECRET_KEY = "supersecretkey"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    class Config:
        env_file = ".env"


settings = Settings()
