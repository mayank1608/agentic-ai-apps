from database.schema_reader import get_schema

class SchemaTool:

    name = "schema_tool"

    def execute(self):

        return get_schema()