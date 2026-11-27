import pandas as pd

from utils.file_name_generator import (
    generate_excel_filename
)

class ExcelTool:

    name = "excel_tool"

    def execute(self, rows, question):

        df = pd.DataFrame(rows)

        # file_name = "output.xlsx"
        file_name = generate_excel_filename(
            question
        )

        pd.DataFrame(rows).to_excel(
            file_name,
            index=False
        )

        return {
            "status": "success",
            "file": file_name,
            "rows": len(rows)
        }