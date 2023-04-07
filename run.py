from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import select

from driver_reporting.database import Database, DatabaseDriverOperations
from driver_reporting.config import HOST, USER, PASSWORD, DATABASE_NAME

def app():
    database = Database(HOST, USER, PASSWORD, DATABASE_NAME)
    driver_operations = DatabaseDriverOperations(database)
    driver_operations.search_drivers(hire_date=datetime(2022, 1, 1), term_date=datetime(2023, 1, 1))

if __name__ == "__main__":
    app()

