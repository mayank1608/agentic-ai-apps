from services.gemini_service import GeminiService
import json

class PlannerAgent:

    def __init__(self):

        self.gemini = GeminiService()

    def decide(self, question):

        prompt = f"""
        You are an AI Agent.

        Available tools:

        1. schema_tool
        Use when user asks for
        table structure, schema, columns.

        2. sql_tool
        Use when user wants data.

        3. chart_tool
        Use when user asks for chart,
        graph, visualization.

        4. excel_tool
        Use when user asks export,
        spreadsheet, excel.
        
        5. tavily_tool
        Use when user asks Weather, 
        News, Current events, Internet search, 
        Latest information, non-database questions.
        
        6. chat_tool
        Use when user asks general reasoning, 
        programming, greetings, 
        non-database questions.

        Return JSON:

        {{
        "tools": []
        }}

        Question:
        {question}
        """

        response = self.gemini.ask(prompt)
        
        response = response.replace("```json","")
        response = response.replace("```","")

        return json.loads(response)