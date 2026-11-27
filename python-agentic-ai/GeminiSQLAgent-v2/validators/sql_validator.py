def validate_sql(sql):

    sql = sql.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    forbidden = [
        "DELETE",
        "UPDATE",
        "INSERT",
        "DROP",
        "ALTER",
        "TRUNCATE"
    ]

    upper_sql = sql.upper()

    for keyword in forbidden:

        if keyword in upper_sql:

            raise Exception(
                f"Forbidden keyword: {keyword}"
            )

    if not upper_sql.startswith("SELECT"):

        raise Exception(
            "Only SELECT queries are allowed"
        )

    return sql