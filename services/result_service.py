import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Menu


async def get_results(db: AsyncSession):
    today = datetime.date.today()
    result = await db.execute(select(Menu).filter(Menu.day == today))
    return {"menus": [menu.id for menu in result.scalars().all()]}
