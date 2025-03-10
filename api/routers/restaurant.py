from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from db.schemas import RestaurantCreate, RestaurantResponse
from services.rest_service import create_restaurant

router = APIRouter()


@router.post("/", response_model=RestaurantResponse)
async def add_restaurant(restaurant_data: RestaurantCreate, db: AsyncSession = Depends(get_db)):
    return await create_restaurant(db, restaurant_data)
