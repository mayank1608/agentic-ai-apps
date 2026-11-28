from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    DB_SERVER = "BRT3L00086\\SQLEXPRESS"

    DB_NAME = "CompanyDB"