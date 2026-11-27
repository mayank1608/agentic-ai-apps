import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def generate_sql(question, schema):

    system_prompt = f"""
    You are an SQL expert.

    Database Schema:
    {schema}
    
    Rules:
    1. Return only SQL.
    2. Do not use markdown.
    3. Do not use ```sql.
    4. Do not provide explanations.
    5. SQL Server syntax only.

    Question:
    {question}

    Return SQL only.
    """
    
    print("API KEY =", os.getenv("GEMINI_API_KEY"))
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=system_prompt
    )

    return response.text