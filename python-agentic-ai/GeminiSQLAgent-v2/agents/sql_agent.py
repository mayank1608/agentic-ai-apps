from agents.planner_agent import PlannerAgent

from services.sql_generator import generate_sql
from services.answer_generator import generate_answer

from database.schema_reader import get_schema

from validators.sql_validator import validate_sql

from tools.registry import TOOLS

from memory.memory_manager import MemoryManager

from services.gemini_service import GeminiService as gemini


class SQLAgent:

    def __init__(self):

        self.planner = PlannerAgent()

        self.memory = MemoryManager()

    def ask(self, question):

        plan = self.planner.decide(question)

        print("\nPlan:", plan)
        
        if len(plan["tools"]) == 0:
            answer = gemini.ask(question)
            return answer

        schema = get_schema()

        sql = generate_sql(
            question,
            schema
        )

        sql = validate_sql(sql)

        print("\nGenerated SQL:")

        print(sql)

        rows = TOOLS["sql_tool"].execute(sql)

        print("\nRows:")

        print(rows)
        
        if "chat_tool" in plan["tools"] or sql.upper() in [
            "SELECT NULL;",
            "SELECT NULL",
            "NULL"
        ]:
                
            return TOOLS["chat_tool"].execute(
                question
            )
                    
        if "tavily_tool" in plan["tools"]:

            result = TOOLS[
                "tavily_tool"
            ].execute(question)

            return result

        if "chart_tool" in plan["tools"]:

            chart_file = TOOLS["chart_tool"].execute(
                rows
            )

            return f"Chart Generated: {chart_file}"

        if "excel_tool" in plan["tools"]:

            excel_file = TOOLS["excel_tool"].execute(
                rows,
                question
            )

            return f"Excel Generated: {excel_file}"

        answer = generate_answer(
            question,
            rows
        )

        self.memory.save(
            question,
            answer
        )

        return answer