from fastapi import FastAPI
from api.routers import auth, restaurant, menus, employee, result

app = FastAPI(title="Restaurant API")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(restaurant.router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(menus.router, prefix="/menus", tags=["Menus"])
app.include_router(employee.router, prefix="/employees", tags=["Employees"])
app.include_router(result.router, prefix="/results", tags=["Results"])
