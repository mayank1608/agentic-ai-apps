import pyodbc

def get_schema():

    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=BRT3L00086\\SQLEXPRESS;"
        "Database=CompanyDB;"
        "Trusted_Connection=yes;"
    )

    cursor = conn.cursor()

    query = """
    SELECT
        TABLE_NAME,
        COLUMN_NAME,
        DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    ORDER BY TABLE_NAME
    """

    cursor.execute(query)

    schema = []

    for row in cursor.fetchall():
        schema.append(
            f"{row.TABLE_NAME} | {row.COLUMN_NAME} | {row.DATA_TYPE}"
        )

    conn.close()

    return "\n".join(schema)