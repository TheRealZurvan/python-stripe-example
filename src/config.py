from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    stripe_secret_key: str = Field(..., alias='STRIPE_SECRET_KEY')
    payment_success_url: str = Field(default='http://localhost:8000/success', alias='PAYMENT_SUCCESS_URL')
    payment_cancel_url: str = Field(default='http://localhost:8000/cancel', alias='PAYMENT_CANCEL_URL')

    class Config:
        env_file = '.env'
        case_sensitive = False
        extra = 'ignore'


settings = Settings()
