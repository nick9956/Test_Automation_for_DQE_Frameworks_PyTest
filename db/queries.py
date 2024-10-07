def average_value_query(column_name, table_name):
    """Query to get the average value of a specified column in a specified table."""
    return f"SELECT AVG({column_name}) FROM {table_name}"


def range_value_query(column_name, table_name, min_val, max_val):
    """Query to get all rows where the specified column's value is between min_val and max_val."""
    return f"SELECT * FROM {table_name} WHERE {column_name} BETWEEN {min_val} AND {max_val}"
