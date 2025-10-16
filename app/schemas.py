from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CarBase(BaseModel):
    make: str = Field(..., min_length=1, max_length=50, description="Car manufacturer")
    model: str = Field(..., min_length=1, max_length=100, description="Car model")
    year: int = Field(..., ge=1900, le=2030, description="Manufacturing year")
    price: float = Field(..., gt=0, description="Car price in USD")
    mileage: Optional[int] = Field(None, ge=0, description="Car mileage")
    color: Optional[str] = Field(None, max_length=30, description="Car color")
    description: Optional[str] = Field(None, description="Car description")

class CarCreate(CarBase):
    pass

class CarResponse(CarBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True