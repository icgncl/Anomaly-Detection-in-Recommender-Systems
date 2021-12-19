class SqlStrings:
    groupby_rating_sql = """
    SELECT overall, count(*) 
    FROM magazine_table
    GROUP BY overall
    """