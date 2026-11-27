from database.query_executor import execute_query

class SQLTool:

    name = "sql_tool"

    def execute(self, sql):

        return execute_query(sql)