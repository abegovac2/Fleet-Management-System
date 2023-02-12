from fastapi import FastAPI
from routers import vehicle, driver, trip, assign
from data_access.database import Base, engine
#import uvicorn
from config import APP_PORT

#Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(vehicle.router)
app.include_router(driver.router)
app.include_router(trip.router)
app.include_router(assign.router)

#if __name__ == "main":
#    uvicorn.run(app, host="0.0.0.0", port=APP_PORT)