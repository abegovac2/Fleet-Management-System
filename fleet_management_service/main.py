from fastapi import FastAPI
from routers import vehicle, driver, trip, assign
from multiprocessing import Process
from driver_update_process import update_driver_points
import config


app = FastAPI()


@app.on_event("startup")
def create_driver_update_process():
    new_process = Process(target=update_driver_points, args=(
        [
        config.RMQ_DRIVER_NAME,
        config.RMQ_DRIVER_EXCHANGE,
        config.RMQ_DRIVER_ROUTING_KEY,
        ]
    ))
    
    new_process.start()


app.include_router(vehicle.router)
app.include_router(driver.router)
app.include_router(trip.router)
app.include_router(assign.router)