from dotenv import load_dotenv
import os


load_dotenv

class Settings:
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    groq_api_key = os.getenv('GROQ_API_KEY')

    settings= Settings()
    