import pyodbc
from config.settings import Settings

def get_connection():

    return pyodbc.connect(
        f"Driver={{ODBC Driver 17 for SQL Server}};"
        f"Server={Settings.DB_SERVER};"
        f"Database={Settings.DB_NAME};"
        "Trusted_Connection=yes;"
    )