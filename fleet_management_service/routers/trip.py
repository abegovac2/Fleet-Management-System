from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from data_access.dto_models import Trip
from data_access.repositories import TripRepository, generate_repository
from typing import List

router = APIRouter(
    prefix="/api/v1/trip",
    tags=["Trip"]
)


@router.get("/list", response_description = "Get all trips", response_model=List[Trip])
def get_vehicle(_repo: TripRepository = Depends(generate_repository(TripRepository))):
    query_res = _repo.get_all()
    if query_res == None:
        query_res = []
    return query_res
    
@router.get("/{id}", response_description = "Get a single trip", response_model=Trip)
def get_vehicle(id: int, _repo: TripRepository = Depends(generate_repository(TripRepository))):
    query_res = _repo.get_by_id(id)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trip with id: {id} does not exist"
        )
    return query_res

@router.post("/", response_description = "Create a new trip", response_model=Trip)
def post_vehicle(trip: Trip, _repo: TripRepository = Depends(generate_repository(TripRepository))):
    query_res = _repo.insert(trip)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Driver with id: {trip.id} already exists"
        )
    return JSONResponse(
            status_code=status.HTTP_201_CREATED, 
            content=query_res.dict()
            )

@router.put("/{id}", response_description="Edit existing trip", response_model=Trip)
def put_vehicle(id: int, trip: Trip, _repo: TripRepository = Depends(generate_repository(TripRepository))):
    query_res = _repo.update(id, trip)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trip with id: {id} does not exist"
        )
    return query_res

@router.delete("/{id}", response_description="Delete existing trip", response_model=int)
def delete_vehicle(id: int, _repo: TripRepository = Depends(generate_repository(TripRepository))):
    query_res = _repo.delete(id)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Trip with id: {id} does not exist"
        )
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content=f"Trip with id: {id} successfuly deleted"
    )