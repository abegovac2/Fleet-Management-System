from pydantic import BaseModel
from typing import Optional

class CustomBaseModel(BaseModel):
    class Config:
        orm_mode=True

class Vehicle(CustomBaseModel):
    id: Optional[int]
    type: str
    registration: str

class Trip(CustomBaseModel):
    id: Optional[int]
    departure_geo_point: str
    destination_geo_point: str
    
class Driver(CustomBaseModel):
    id: Optional[int]
    full_name: str
    points: int