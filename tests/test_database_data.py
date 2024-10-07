import pytest
import logging
from db.queries import average_value_query, range_value_query


@pytest.mark.database
@pytest.mark.parametrize("column,table,expected_result", [
    ('salary', 'hr.employees', 8060.000000),
    ('location_id', 'hr.departments', 1890),
    ('region_id', 'hr.countries', 2)
])
def test_average_value(db, column, table, expected_result):
    """
    Test to verify that the average value calculation for a given column and table is correct.
    Parameters:
    - column: the name of the column to calculate the average
    - table: the table from which to calculate the average
    - expected_result: the expected average value
    """
    query = average_value_query(column, table)
    result = db.execute_query(query)
    logging.info(f"Testing average value for {column} in {table}")
    logging.info(f"Expected value: {expected_result}, Actual value: {result[0][0]}")
    assert result is not None, "Query failed to return any results"
    assert len(result) == 1 and result[0][0] == expected_result, f"Expected average value of {expected_result}, got {result[0][0]}"


@pytest.mark.database
@pytest.mark.parametrize("column,table,min_val,max_val,expected_count", [
    ('salary', 'hr.employees', 20000, 100000, 1),
    ('min_salary', 'hr.jobs', 2000, 3000, 4),
    ('location_id', 'hr.departments', 1500, 1800, 7)
])
def test_value_in_range(db, column, table, min_val, max_val, expected_count):
    """
    Test to verify that the number of records falling within a specified range for a given column and table is correct.
    Parameters:
    - column: the name of the column
    - table: the table to query
    - min_val: the minimum value of the range
    - max_val: the maximum value of the range
    - expected_count: the expected number of records within the range
    """
    query = range_value_query(column, table, min_val, max_val)
    results = db.execute_query(query)
    logging.info(f"Testing range for {column} in {table} between {min_val} and {max_val}")
    logging.info(f"Expected count: {expected_count}, Actual count: {len(results)}")
    assert results is not None, "Query failed to return any results"
    assert len(results) == expected_count, f"Expected {expected_count} rows, got {len(results)}"
