from pydantic import BaseModel
from datetime import date


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class RestaurantCreate(BaseModel):
    name: str
    owner_id: int


class RestaurantResponse(RestaurantCreate):
    id: int


class MenuCreate(BaseModel):
    day: date
    restaurant_id: int


class MenuResponse(BaseModel):
    id: int
    day: date
    restaurant_id: int

    class Config:
        from_attributes = True


class EmployeeCreate(BaseModel):
    name: str
    role: str


class EmployeeResponse(BaseModel):
    id: int
    name: str
    role: str

    class Config:
        from_attributes = True
