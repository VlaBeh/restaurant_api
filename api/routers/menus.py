from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from db.schemas import MenuCreate, MenuResponse
from services.menu_service import create_menu, get_current_menu

router = APIRouter()


@router.post("/", response_model=MenuResponse)
async def upload_menu(menu_data: MenuCreate, db: AsyncSession = Depends(get_db)):
    return await create_menu(db, menu_data)


@router.get("/current", response_model=MenuResponse)
async def get_today_menu(db: AsyncSession = Depends(get_db)):
    return await get_current_menu(db)