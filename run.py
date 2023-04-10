from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import select

from driver_reporting.database import Database, DriverOperations
from driver_reporting.config import HOST, USER, PASSWORD, DATABASE_NAME

def app():
    database = Database(HOST, USER, PASSWORD, DATABASE_NAME)
    driver_operations = DriverOperations(database)

if __name__ == "__main__":
    app()

