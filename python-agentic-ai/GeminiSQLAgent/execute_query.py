import pyodbc
from sqlalchemy import sql

def execute_query(sql):    
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=BRT3L00086\\SQLEXPRESS;"
        "Database=CompanyDB;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows


