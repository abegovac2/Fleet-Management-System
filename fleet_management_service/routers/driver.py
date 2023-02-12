from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from data_access.dto_models import Driver
from data_access.repositories import DriverRepository, generate_repository
from typing import List

router = APIRouter(
    prefix="/api/v1/driver",
    tags=["Driver"]
)


@router.get("/list", response_description = "Get all drivers", response_model=List[Driver])
def get_vehicle(_repo: DriverRepository = Depends(generate_repository(DriverRepository))):
    query_res = _repo.get_all()
    if query_res == None:
        query_res = []
    return query_res
    
@router.get("/{id}", response_description = "Get a single driver", response_model=Driver)
def get_vehicle(id: int, _repo: DriverRepository = Depends(generate_repository(DriverRepository))):
    query_res = _repo.get_by_id(id)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Driver with id: {id} does not exist"
        )
    return query_res

@router.post("/", response_description = "Create a new driver", response_model=Driver)
def post_vehicle(driver: Driver, _repo: DriverRepository = Depends(generate_repository(DriverRepository))):
    query_res = _repo.insert(driver)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Driver with id: {driver.id} already exists"
        )
    return JSONResponse(
            status_code=status.HTTP_201_CREATED, 
            content=query_res.dict()
            )

@router.put("/{id}", response_description="Edit existing driver", response_model=Driver)
def put_vehicle(id: int, driver: Driver, _repo: DriverRepository = Depends(generate_repository(DriverRepository))):
    query_res = _repo.update(id, driver)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Driver with id: {id} does not exist"
        )
    return query_res

@router.delete("/{id}", response_description="Delete existing driver", response_model=int)
def delete_vehicle(id: int, _repo: DriverRepository = Depends(generate_repository(DriverRepository))):
    query_res = _repo.delete(id)
    if query_res == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Driver with id: {id} does not exist"
        )
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT,
        content=f"Driver with id: {id} successfuly deleted"
    )