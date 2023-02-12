from pydantic import BaseModel

class StartTrip(BaseModel):
    trip_id: int
    vehicle_id: int
    driver_id: int