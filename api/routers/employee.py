from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from db.schemas import EmployeeCreate, EmployeeResponse
from services.employee_service import create_employee

router = APIRouter()


@router.post("/register", response_model=EmployeeResponse)
async def add_employee(employee_data: EmployeeCreate, db: AsyncSession = Depends(get_db)):
    return await create_employee(db, employee_data)
