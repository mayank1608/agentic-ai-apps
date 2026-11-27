import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def explain_answer(question, rows):    
    prompt = f"""
    Question:
    {question}

    Data:
    {rows}

    Explain the answer in simple English.
    """

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text