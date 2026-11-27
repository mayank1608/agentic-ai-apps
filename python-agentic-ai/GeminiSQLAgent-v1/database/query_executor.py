from database.connection import get_connection

def execute_query(sql):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(sql)

    rows = cursor.fetchall()

    conn.close()

    return rows