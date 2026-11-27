def validate_sql(sql):

    sql = sql.strip().upper()

    forbidden_words = [
        "DELETE",
        "DROP",
        "TRUNCATE",
        "ALTER",
        "UPDATE",
        "INSERT"
    ]

    for word in forbidden_words:
        if word in sql:
            raise Exception(
                f"Forbidden SQL keyword detected: {word}"
            )

    if not sql.startswith("SELECT"):
        raise Exception(
            "Only SELECT queries are allowed"
        )

    return True