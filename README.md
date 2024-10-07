# Project Setup Guide

## Prerequisites
Before initiating the project setup, make sure to have the following prerequisites installed on your system:
1. **MSSQL ODBC Driver**: The project requires the MSSQL ODBC driver for database connectivity. Download and install it from the [Microsoft official website](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

2. **Database Configuration**: Update your database configuration details and credentials in the provided database config file to establish a connection with your MSSQL database.

## Setting Up a Virtual Environment
For better management of project dependencies, it is advisable to use a virtual environment. Here are the steps to set up a virtual environment:

1. **Install virtualenv** (if not installed):
   ```
   pip install virtualenv
   ```

2. **Create a Virtual Environment**:
   In the project directory, execute:
   ```
   virtualenv venv
   ```

3. **Activate the Virtual Environment**:
   - For Windows users:
     ```
     .\venv\Scripts\activate
     ```

## Installing Dependencies
This project utilizes Poetry for managing dependencies. Follow these steps to install the necessary dependencies:

1. **Install Poetry**: If Poetry is not already installed, follow the installation guide on the [official Poetry website](https://python-poetry.org/docs/#installation).

2. **Install Project Dependencies**: With Poetry installed and the virtual environment activated, install all required dependencies by running:
   ```
   poetry install
   ```

### List of Dependencies
- **Python** version 3.12
- **pyodbc** version 5.1.0
- **pytest** version 8.3.3 (dev dependency)
- **pytest-html** version 4.1.1 (dev dependency)

## Running Tests
To run all tests in the project folder, execute the following command:
```
pytest
```

The html report is generated in the output folder automaticall.

## Build System
This project uses Poetry as the build system with the following configuration:
- **Requires**: `poetry-core`
- **Build Backend**: `poetry.core.masonry.api`

Ensure you have properly configured the build system by ensuring the `pyproject.toml` file is set up correctly as per the above configuration.