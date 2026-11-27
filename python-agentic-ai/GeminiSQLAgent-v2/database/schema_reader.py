from database.connection import get_connection

def get_schema():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            TABLE_NAME,
            COLUMN_NAME,
            DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        ORDER BY TABLE_NAME
    """)

    schema = []

    for row in cursor.fetchall():

        schema.append(
            f"{row.TABLE_NAME} | {row.COLUMN_NAME} | {row.DATA_TYPE}"
        )

    conn.close()

    return "\n".join(schema)