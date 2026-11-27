# db_connection.py

import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=BRT3L00086\\SQLEXPRESS;"
    "Database=CompanyDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

cursor.execute("SELECT GETDATE()")

print(cursor.fetchone())

conn.close()