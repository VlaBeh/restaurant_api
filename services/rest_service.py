from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Restaurant
from db.schemas import RestaurantCreate


async def create_restaurant(db: AsyncSession, restaurant_data: RestaurantCreate):
    new_restaurant = Restaurant(name=restaurant_data.name, owner_id=restaurant_data.owner_id)
    db.add(new_restaurant)
    await db.commit()
    await db.refresh(new_restaurant)
    return new_restaurant