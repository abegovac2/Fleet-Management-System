from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from model import StartTrip
import requests
import config
from multiprocessing import Process
from generator_process import start_trip_process
#import uvicorn

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
        config.RABBIT_QUEUE,
        config.RABBIT_EXCHANGE,
        config.RABBIT_ROUTING_KEY,
        trip_data.driver_id,
        ]
    ))
    
    new_process.start()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Trip started"})

#if __name__ == "main":
#    uvicorn.run(app, host="0.0.0.0", port=config.APP_PORT)