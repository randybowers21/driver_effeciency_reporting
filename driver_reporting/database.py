#PYTHON
from datetime import datetime
from datetime import date
#3RD PARTY
import sqlalchemy
from sqlalchemy import create_engine, select, update, and_
from sqlalchemy.orm import Session
#LOCAL
import driver_reporting.models as models
import driver_reporting.helper_functions as helpers
import driver_reporting.errors as errors

class Database:
    def __init__(self, host, user, password, database):
        self.sqlalchemy_engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/{database}')

class DriverOperations:
    def __init__(self, database):
        self.database = database

    # def search_driver_by_code(self, driver_code):
    #     with Session(self.database.sqlalchemy_engine) as session:
    #         query = session.query(models.Driver).filter(models.Driver.driver_code == driver_code)
    #         result = session.execute(query)
    #         for driver in result.scalars():
    #             print(f'{driver.driver_code}: {driver.hire_date} - {driver.term_date}')

    # def search_drivers_by_hire_date(self, search_start_date: datetime=helpers.get_first_day_of_current_year(), search_end_date: datetime=datetime.today()):
    #     with Session(self.database.sqlalchemy_engine) as session:
    #         query = session.query(models.Driver) \
    #             .filter(models.Driver.hire_date >= search_start_date, models.Driver.hire_date <= search_end_date) \
    #             .filter(models.Driver.driver_code == ' ') \
    #             .order_by(models.Driver.hire_date)
    #         result = session.execute(query).scalars()
    #         for driver in result:
    #             print(f'{driver.driver_code}: {driver.hire_date} - {driver.term_date}')

    def test_search(self, driver_code:str=None, hire_date: datetime=None, term_date:datetime=None):
        queries = []
        with Session(self.database.sqlalchemy_engine) as session:
            if driver_code:
                queries.append(models.Driver.driver_code == driver_code)
            if hire_date:
                queries.append(models.Driver.hire_date >= hire_date)
            if term_date:
                queries.append(models.Driver.term_date <= term_date)

            query = session.query(models.Driver).filter(*queries)

        result = session.execute(query).scalars()
        for driver in result:
            print(driver)

    def create_driver(self, driver_code:str, fleet_code: str, hire_date: date, term_date: date=None, commit=False):
        with Session(self.database.sqlalchemy_engine) as session:
            #Queries
            new_driver = models.Driver(driver_code=driver_code, hire_date=hire_date.date(), term_date=term_date)
            new_fleet_worked_on = models.FleetWorkedOn(driver_code=driver_code, fleet_code=fleet_code, start_date=hire_date)

            if commit == True:
                print(helpers.DbMessages.create_save_message(f'Driver: {new_driver.driver_code}'))
                print(helpers.DbMessages.create_save_message(f'Fleet Worked On: {new_fleet_worked_on.fleet_code}'))
                session.add_all([new_driver, new_fleet_worked_on])
                session.commit()
            else:
                print(helpers.DbMessages.create_be_sure_to_commit_message(data=f'Driver: {new_driver.driver_code}'))
    
    def update_driver(self, driver_code: str, column_to_change:str, new_value):
        with Session(self.database.sqlalchemy_engine) as session:
            stmt = select(models.Driver).where(models.Driver.driver_code == driver_code)
            #Try to find driver to update
            try:
                found_driver = session.scalars(stmt).one()
            except sqlalchemy.exc.NoResultFound:
                message = errors.ItemNotInDbError(('Driver', driver_code)).message
                print(message)
                return
            #Make changes to found driver based on selected column value
            if column_to_change == 'driver_code':
                found_driver.driver_code = new_value
            elif column_to_change == 'hire_date':
                found_driver.hire_date = new_value
            elif column_to_change == 'term_date':
                found_driver.term_date = new_value

            print(found_driver)
