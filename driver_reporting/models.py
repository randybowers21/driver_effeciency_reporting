#PYTHON
from datetime import datetime
#3RD PARTY
from sqlalchemy import ForeignKey, String, Boolean, Date, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
#LOCAL

class Base(DeclarativeBase):
    pass

class Tractor(Base):
    __tablename__ = 'tractor'
    tractor_code = mapped_column(Integer(), primary_key=True)
    fleet_code = mapped_column(String(20), ForeignKey('fleet.fleet_code'), nullable=False)
    active_date = mapped_column(Date, nullable=False, default=datetime.utcnow().date)
    inactive_date = mapped_column(Date, default=None)

    def __repr__(self):
        return f'Tractor("{self.tractor_code}", Fleet "{self.fleet_code}" In Service: "{self.active_date}")'

class Fleet(Base):
    __tablename__ = 'fleet'
    fleet_code = mapped_column(String(20), primary_key=True)
    fleet_name = mapped_column(String(25), nullable=False)
    is_active = mapped_column(Boolean(), nullable=False, default=True)
    fleet_type = mapped_column(String(10), nullable=False)
    tractors = relationship('Tractor')

    def __repr__(self):
        return f'Fleet("{self.fleet_name}", Code "{self.fleet_code}")'
    
class Driver(Base):
    __tablename__ = 'driver'
    driver_code: Mapped[str] = mapped_column(String(8), primary_key=True)
    hire_date = mapped_column(Date, nullable=False, default=datetime.utcnow().date)
    term_date = mapped_column(Date, default=None)
    fleets = relationship('FleetWorkedOn', lazy=True)

    def __repr__(self):
        return f'Driver("{self.driver_code}", Hired: "{self.hire_date}", {self.fleets})'

class FleetWorkedOn(Base):
    __tablename__ = 'fleet_worked_on'
    driver_code = mapped_column(String(8), ForeignKey('driver.driver_code'), primary_key=True,  nullable=False)
    fleet_code = mapped_column(String(25), ForeignKey('fleet.fleet_code'), primary_key=True,  nullable=False)
    start_date = mapped_column(Date, nullable=False, default=datetime.utcnow().date)
    end_date = mapped_column(Date, default=None)

    # def __repr__(self):
    #     return f'Driver("{self.driver_code}", Fleet: "{self.fleet_code}")'

class DriverWorkWeek(Base):
    __tablename__ = 'driver_work_week'
    week_start = mapped_column(Date, primary_key=True, nullable=False)
    driver_code = mapped_column(String(8), ForeignKey('driver.driver_code'), primary_key=True, nullable=False)
    distance = mapped_column(Integer(), nullable=False)
    fuel_used = mapped_column(Float())
    idle_fuel = mapped_column(Float())
    driving_mpg = mapped_column(Float())
    total_mpg = mapped_column(Float())
    average_speed = mapped_column(Float())
    total_idle_time = mapped_column(Float())
    total_idle_percent = mapped_column(Float())
    intertrip_idle_time = mapped_column(Float())
    intertrip_idle_percent = mapped_column(Float())
    operating_idle_time = mapped_column(Float())
    operating_idle_percent = mapped_column(Float())
    short_idle_time = mapped_column(Float())
    short_idle_percent = mapped_column(Float())
    extended_idle_time = mapped_column(Float())
    extended_idle_percent = mapped_column(Float())
    coast_time = mapped_column(Float())
    coast_percent = mapped_column(Float())
    over_speed_time = mapped_column(Float())
    over_speed_percent = mapped_column(Float())
    over_speed_count = mapped_column(Float())
    over_rpm_time = mapped_column(Float())
    over_rpm_percent = mapped_column(Float())
    over_rpm_count = mapped_column(Float())
    long_over_speed_time = mapped_column(Float())
    long_over_rpm_time = mapped_column(Float())
    engine_time = mapped_column(Float())
    moving_time = mapped_column(Float())
    moving_percent = mapped_column(Float())
    driving_time = mapped_column(Float())
    driving_percent = mapped_column(Float())
    hard_break_time = mapped_column(Float())
    hard_break_count = mapped_column(Float())
    top_gear_time = mapped_column(Float())
    top_gear_percent = mapped_column(Float())
    cruise_control_time = mapped_column(Float())
    cruise_control_percent = mapped_column(Float())

    # def __repr__(self):
    #     return f'Work Week(Driver Code "{self.driver_code}", Week Start: "{self.week_start}")'
    