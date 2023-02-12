from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    registration = Column(String(50))
    

class Driver(Base):
    __tablename__ = 'driver'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    points = Column(Integer)


class Trip(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True)
    departure_geo_point = Column(String(100))
    destination_geo_point = Column(String(100))


class VehicleDrivers(Base):
    __tablename__ = 'vehicle_drivers'
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)
    driver_id = Column(Integer, ForeignKey('driver.id'), primary_key=True)


class VehicleTrips(Base):
    __tablename__ = 'vehicle_trips'
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)
    trip_id = Column(Integer, ForeignKey('trip.id'), primary_key=True)

