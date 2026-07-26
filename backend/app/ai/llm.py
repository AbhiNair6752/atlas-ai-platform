from groq import Groq
from app.config.settings import get_settings

settings = get_settings()

client = Groq(
    api_key=settings.GROQ_API_KEY
)