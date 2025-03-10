import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_upload_menu():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/menus/", json={"day": "2025-03-09", "restaurant_id": 1})
    assert response.status_code == 200
    assert "id" in response.json()


@pytest.mark.asyncio
async def test_get_current_menu():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/menus/current")
    assert response.status_code == 200
    assert "id" in response.json()
