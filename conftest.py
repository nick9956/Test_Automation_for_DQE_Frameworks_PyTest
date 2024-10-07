import pytest
from db.connection import DatabaseLibrary


@pytest.fixture(scope="module")
def db():
    """
    Pytest fixture to manage a database connection.

    This fixture creates an instance of the DatabaseLibrary, connects to the database,
    and then provides that instance to the test functions. After the tests are complete,
    it ensures the database connection is properly closed.

    Yields:
        DatabaseLibrary: An instance of the DatabaseLibrary class, connected to the database.
    """
    db_instance = DatabaseLibrary()
    db_instance.connect_to_database()
    yield db_instance
    db_instance.disconnect_from_database()
