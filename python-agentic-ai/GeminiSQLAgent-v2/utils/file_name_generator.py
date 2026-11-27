from services.gemini_service import GeminiService
from datetime import datetime

gemini = GeminiService()

def generate_excel_filename(question):

    prompt = f"""
    Generate a short filename
    for this request.

    Question:
    {question}

    Rules:
    1. Use lowercase only
    2. Use underscore
    3. No spaces
    4. No file extension
    5. Maximum 5 words

    Examples:

    employee_details
    department_salary_report
    highest_salary_employees

    Return filename only.
    ?"""

    filename = gemini.ask(prompt)

    filename = filename.strip()

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    return f"{filename}_{timestamp}.xlsx"