from fastapi.security import OAuth2PasswordBearer
from pydantic_settings import BaseSettings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Settings(BaseSettings):
    DATABASE_URL: str
    COMPANY_CNPJ: str
    ALLOWED_ORIGINS: str

    class Config:
        env_file = ".env"


settings = Settings()
