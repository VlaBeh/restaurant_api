from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Employee
from core.security import verify_password, create_access_token


async def authenticate_user(db: AsyncSession, username: str, password: str):
    result = await db.execute(select(Employee).filter(Employee.name == username))
    user = result.scalars().first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None
