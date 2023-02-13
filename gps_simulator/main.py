from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from model import StartTrip
import requests
import config
from multiprocessing import Process
from generator_process import start_trip_process

app = FastAPI()

@app.post("/start-trip")
def start_trip(trip_data: StartTrip):
    url = f"{config.MANAGEMENT_SERVICE}/trip/{trip_data.trip_id}"
    print(url)
    response = requests.get(url = url)
    trip = response.json()
    if response.status_code != 200:
        return JSONResponse(
            status_code=response.status_code, 
            content=trip)

    new_process = Process(target=start_trip_process, args=(
        [
        trip_data.vehicle_id,
        trip["departure_geo_point"],
        trip["destination_geo_point"],
        config.RMQ_POINTS_NAME,
        config.RMQ_POINTS_EXCHANGE,
        config.RMQ_POINTS_EXCHANGE,
        trip_data.driver_id,
        ]
    ))
    
    new_process.start()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Trip started"})