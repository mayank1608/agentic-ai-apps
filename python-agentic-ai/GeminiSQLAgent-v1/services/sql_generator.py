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

    Rules:
    1. SQL Server syntax only
    2. Return only SQL
    3. No markdown
    4. No explanation
    
    Rules:
    - Consider common abbreviations.
    - IT means Information Technology.
    - HR means Human Resources.
    - Use available sample values when filtering.

    Question:
    {question}
    """

    return gemini.ask(prompt)