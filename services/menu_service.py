import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Menu
from db.schemas import MenuCreate


async def create_menu(db: AsyncSession, menu_data: MenuCreate):
    new_menu = Menu(day=menu_data.day, restaurant_id=menu_data.restaurant_id)
    db.add(new_menu)
    await db.commit()
    await db.refresh(new_menu)
    return new_menu


async def get_current_menu(db: AsyncSession):
    today = datetime.date.today()
    result = await db.execute(select(Menu).filter(Menu.day == today))
    return result.scalars().first()
