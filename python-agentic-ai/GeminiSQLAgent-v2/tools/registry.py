from tools.sql_tool import SQLTool
from tools.schema_tool import SchemaTool
from tools.chart_tool import ChartTool
from tools.excel_tool import ExcelTool

TOOLS = {
    "sql_tool": SQLTool(),
    "schema_tool": SchemaTool(),
    "chart_tool": ChartTool(),
    "excel_tool": ExcelTool()
}