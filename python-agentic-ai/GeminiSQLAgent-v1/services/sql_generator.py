from services.gemini_service import GeminiService

gemini = GeminiService()

def generate_sql(question, schema):

    prompt = f"""
    You are a SQL Server expert.

    Database Schema:
    {schema}
    
    Important Values:
    DepartmentName can contain:
    - Human Resources
    - Information Technology
    - Finance
    - Marketing

    User may use abbreviations:
    IT = Information Technology
    HR = Human Resources

    Rules:
    1. SQL Server syntax only
    2. Return only SQL
    3. No markdown
    4. No explanation

    Question:
    {question}
    """

    return gemini.ask(prompt)