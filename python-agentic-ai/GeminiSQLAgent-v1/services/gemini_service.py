from google import genai
from config.settings import Settings

class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=Settings.GEMINI_API_KEY
        )

    def ask(self, prompt):

        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text