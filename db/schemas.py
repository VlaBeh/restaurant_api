from pydantic import BaseModel


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
