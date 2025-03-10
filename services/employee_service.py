from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Employee
from db.schemas import EmployeeCreate


async def create_employee(db: AsyncSession, employee_data: EmployeeCreate):
    new_employee = Employee(name=employee_data.name, role=employee_data.role, password=employee_data.password)
    db.add(new_employee)
    await db.commit()
    await db.refresh(new_employee)
    return new_employee
