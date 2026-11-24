import os

from mssql_python import connect


def get_recent_work_items_sync(
    assigned_to: str,
) -> list[dict]:
    connection_string = os.getenv("SQL_CONNECTION_STRING")

    if not connection_string:
        raise RuntimeError(
            "SQL_CONNECTION_STRING is not configured"
        )

    connection = connect(connection_string)
    cursor = connection.cursor()

    try:
        query = """
        SELECT TOP 10
            Id,
            Title,
            Status,
            DueDate
        FROM dbo.WorkItems
        WHERE AssignedTo = ?
        ORDER BY DueDate ASC;
        """

        cursor.execute(query, (assigned_to,))

        column_names = [
            description[0]
            for description in cursor.description
        ]

        rows = cursor.fetchall()

        return [
            dict(zip(column_names, row))
            for row in rows
        ]

    finally:
        cursor.close()
        connection.close()