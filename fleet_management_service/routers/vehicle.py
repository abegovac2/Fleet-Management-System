from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from data_access.dto_models import Vehicle
from data_access.repositories import VehicleRepository, generate_repository
from typing import List

router = APIRouter(
    prefix="/api/v1/vehicle",
    tags=["Vehicle"],
)


@router.get("/list", response_description = "Get all vehicles", response_model=List[Vehicle])
def get_vehicle(_repo: VehicleRepository = Depends(generate_repository(VehicleRepository))):
    query_res = _repo.get_all()
    if query_res == None:
        query_res = []
    return query_res
    
@router.get("/{id}", response_description = "Get a single vehicle", response_model=Vehicle)
def get_vehicle(id: int, _repo: VehicleRepository = Depends(generate_repository(VehicleRepository))):
    query_res = _repo.get_by_id(id)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with id: {id} does not exist"
        )
    return query_res

@router.post("/", response_description = "Create a new vehicle", response_model=Vehicle)
def post_vehicle(vehicle: Vehicle, _repo: VehicleRepository = Depends(generate_repository(VehicleRepository))):
    query_res = _repo.insert(vehicle)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Driver with id: {vehicle.id} already exists"
        )
    return JSONResponse(
            status_code=status.HTTP_201_CREATED, 
            content=query_res.dict()
            )

@router.put("/{id}", response_description="Edit existing vehicle", response_model=Vehicle)
def put_vehicle(id: int, vehicle: Vehicle, _repo: VehicleRepository = Depends(generate_repository(VehicleRepository))):
    query_res = _repo.update(id, vehicle)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with id: {id} does not exist"
        )
    return query_res

@router.delete("/{id}", response_description="Delete existing vehicle")
def delete_vehicle(id: int, _repo: VehicleRepository = Depends(generate_repository(VehicleRepository))):
    query_res = _repo.delete(id)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Vehicle with id: {id} does not exist"
        )
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content=f"Vehicle with id: {id} successfuly deleted"
    )