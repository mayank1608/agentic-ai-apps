from services.gemini_service import GeminiService

gemini = GeminiService()

def explain_answer(question, rows):

    prompt = f"""
    Question:
    {question}

    Data:
    {rows}

    Generate a business-friendly answer.
    """

    return gemini.ask(prompt)