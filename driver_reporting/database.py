#PYTHON
from datetime import datetime
#3RD PARTY
from sqlalchemy import create_engine, select, and_
from sqlalchemy.orm import Session
#LOCAL
import driver_reporting.models as models

class Database:
    def __init__(self, host, user, password, database):
        self.sqlalchemy_engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

class DatabaseDriverOperations:
    def __init__(self, database):
        self.database = database

    def search_driver_by_code(self, driver_code):
        with Session(self.database.sqlalchemy_engine) as session:
            query = session.query(models.Driver).filter(models.Driver.driver_code == driver_code)
            result = session.execute(query)
            for driver in result.scalars():
                print(f'{driver.driver_code}: {driver.hire_date} - {driver.term_date}')

    def search_drivers(self, driver_code: str='', hire_date: datetime=None, term_date: datetime=None):
        with Session(self.database.sqlalchemy_engine) as session:
            query = session.query(models.Driver).filter(models.Driver.hire_date >= hire_date, models.Driver.term_date <= term_date, models.Driver.driver_code.like('') == driver_code)
            print(query)
            result = session.execute(query).scalar()
            for driver in result:
                print(f'{driver.driver_code}: {driver.hire_date} - {driver.term_date}')