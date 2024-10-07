import os
import pyodbc
import configparser


class DatabaseLibrary:
    _instance = None

    def __new__(cls):
        # Implementing Singleton pattern to ensure only one instance of DatabaseLibrary exists.
        if cls._instance is None:
            cls._instance = super(DatabaseLibrary, cls).__new__(cls)
            cls._instance.conn = None  
            cls._instance.cursor = None  
        return cls._instance

    def connect_to_database(self):
        config = configparser.ConfigParser()
        # Get the directory of the current script to locate the configuration file.
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # Construct the path to the config file.
        config_path = os.path.join(dir_path, 'db.cfg')
        config.read(config_path)

        try:
            # Extract database configuration details from the config file.
            server = config['DatabaseConfig']['server']
            database = config['DatabaseConfig']['database']
            username = config['DatabaseConfig']['username']
            password = config['DatabaseConfig']['password']
        except KeyError as e:
            print(f"Configuration section or key missing: {e}")
            return

        # Connection string using ODBC Driver 17 for SQL Server
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes'
        try:
            self.conn = pyodbc.connect(connection_string)
            self.cursor = self.conn.cursor()
            print("Connected to database successfully")
        except Exception as e:
            print(f"Failed to connect to database: {e}")
            self.conn = None
            self.cursor = None

    def disconnect_from_database(self):
        # Close the database connection if it exists.
        if self.conn:
            self.conn.close()
            print("Disconnected from database")

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_non_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()
