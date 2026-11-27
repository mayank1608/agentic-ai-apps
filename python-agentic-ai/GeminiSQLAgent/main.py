from execute_query import execute_query
from explain_answer import explain_answer
from get_schema import get_schema
from sql_generator import generate_sql
from sql_validator import validate_sql


question = input("Ask Question: ")

schema = get_schema()

print(schema)

sql = generate_sql(
    question,
    schema
)

print(sql)

allowed = validate_sql(sql)
print(f"allowed: {allowed}")
if allowed:
    rows = execute_query(sql)

    answer = explain_answer(
        question,
        rows
    )

    print(answer)
