from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from data_access.repositories import AssigmentRepository, generate_repository

router = APIRouter(
    prefix="/api/v1/assign",
    tags=["Assignation"]
)


@router.post("/driver/{driver_id}/vehicle/{vehicle_id}")
def assign_driver_vehicle(driver_id: int, vehicle_id: int, _repo: AssigmentRepository = Depends(generate_repository(AssigmentRepository))):
    query_res = _repo.insert_vehicle_driver(vehicle_id, driver_id)
    if query_res == "Inserted":
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "Successfuly assigned driver: {driver_id} to vehicle: {vehicle_id}"}
        )
    elif query_res == "Duplicate":
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Driver id: {driver_id} is already assigned to vehicle id:{vehicle_id}!"
            )
    else:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No such driver or vehicle registerd in the system!"
            )


@router.post("/trip/{trip_id}/vehicle/{vehicle_id}")
def assign_driver_vehicle(trip_id: int, vehicle_id: int, _repo: AssigmentRepository = Depends(generate_repository(AssigmentRepository))):
    query_res = _repo.insert_vehicle_driver(vehicle_id, trip_id)
    if query_res == "Inserted":
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"message": "Successfuly assigned vehicle: {vehicle_id} to trip: {trip_id}"}
        )
    elif query_res == "Duplicate":
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Trip id: {trip_id} is already assigned to vehicle id: {vehicle_id}!"
            )
    else:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No such trip or vehicle registerd in the system!"
            )