from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app.models import Car
from app.schemas import CarCreate, CarResponse

router = APIRouter(prefix="/cars", tags=["cars"])

@router.get("/", response_model=List[CarResponse])
def get_cars(db: Session = Depends(get_db)):
    """Get all cars"""
    cars = db.query(Car).all()
    return cars

@router.get("/{car_id}", response_model=CarResponse)
def get_car(car_id: int, db: Session = Depends(get_db)):
    """Get a specific car by ID"""
    car = db.query(Car).filter(Car.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.post("/", response_model=CarResponse, status_code=201)
def create_car(car_data: CarCreate, db: Session = Depends(get_db)):
    """Create a new car"""
    # Create new car instance
    db_car = Car(
        make=car_data.make,
        model=car_data.model,
        year=car_data.year,
        price=car_data.price,
        mileage=car_data.mileage,
        color=car_data.color,
        description=car_data.description
    )
    
    # Add to database
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    
    return db_car
