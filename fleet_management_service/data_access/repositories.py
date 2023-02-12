from .models import Vehicle, Trip, Driver, VehicleDrivers, VehicleTrips
from .database import SessionLocal
from sqlalchemy.exc import IntegrityError

class BaseRepository:
    def __init__(self, _Model_, db):
        self._Model_ = _Model_
        self._db_ = db

    def get_all(self):
        return self._db_.query(self._Model_).all()
    
    def get_by_id(self, id: int):
        return self._db_.query(self._Model_).get(id)

    def insert(self, data):
        try:
            new_data = data.dict()
            del new_data["id"]
            insert_object = self._Model_(**new_data)
        except:
            return None
        self._db_.add(insert_object)
        self._db_.commit()
        data.id = insert_object.id
        return data

    def update(self, id: int, data):
        update_q = self._db_.query(self._Model_).filter(self._Model_.id == id)
        if(update_q.first() == None):
            return None
        new_data = data.dict()
        del new_data["id"]
        update_q.update(new_data)
        self._db_.commit()
        return update_q.first()

    def delete(self, id: int):
        delete_q = self._db_.query(self._Model_).filter(self._Model_.id == id)
        if(delete_q.first() == None):
            return None
        delete_q.delete()
        self._db_.commit()
        return id


class VehicleRepository(BaseRepository):
    def __init__(self, db) -> None:
        super().__init__(Vehicle, db)

class TripRepository(BaseRepository):
    def __init__(self, db) -> None:
        super().__init__(Trip, db)

class DriverRepository(BaseRepository):
    def __init__(self, db) -> None:
        super().__init__(Driver, db)

class AssigmentRepository:
    def __init__(self, db) -> None:
        self._db_ = db

    def insert_vehicle_driver(self, vehicle_id: int, driver_id: int):
        insert_val = VehicleDrivers(vehicle_id = vehicle_id, driver_id = driver_id)
        try:
            self._db_.add(insert_val)
            self._db_.commit()
            return "Inserted"
        except IntegrityError as error:
            if error.orig.args[0].startswith("duplicate"): return "Duplicate"
            else: return "Invalid"

    def insert_vehicle_trip(self, vehicle_id: int, trip_id: int):
        insert_val = VehicleTrips(vehicle_id = vehicle_id, trip_id = trip_id)
        try:
            self._db_.add(insert_val)
            self._db_.commit()
            return "Inserted"
        except IntegrityError as error:
            if error.orig.args[0].startswith("duplicate"): return "Duplicate"
            else: return "Invalid"


def generate_repository(RepositoryClass):
    def generator():
        db = SessionLocal()
        try:
            yield RepositoryClass(db)
        finally:
            db.close()
    return generator
    

