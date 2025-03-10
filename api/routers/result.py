from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from services.result_service import get_results

router = APIRouter()


@router.get("/", response_model=dict)
async def get_daily_results(db: AsyncSession = Depends(get_db)):
    return await get_results(db)