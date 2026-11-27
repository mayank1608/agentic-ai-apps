from database.schema_reader import get_schema
from database.query_executor import execute_query

from services.gemini_service import GeminiService
from services.sql_generator import generate_sql
from services.answer_generator import explain_answer

from validators.sql_validator import validate_sql

class SQLAgent:

    def ask(self, question):

        print("\nReading schema...")

        schema = get_schema()

        print(schema)

        print("\nGenerating SQL...")

        sql = generate_sql(
            question,
            schema
        )

        sql = validate_sql(sql)

        print("\nGenerated SQL:")

        print(sql)

        rows = execute_query(sql)

        print("\nRows:")

        print(rows)
        
        if len(rows) == 0:
            prompt = f"""
            User Question:
            {question}

            SQL Generated:
            {sql}

            Query Result:
            No rows found.

            Explain possible reasons in simple language.
            """
            
            gemini = GeminiService()
            return gemini.ask(prompt)

        answer = explain_answer(
            question,
            rows
        )

        return answer
