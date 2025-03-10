import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_create_restaurant():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/restaurants/", json={"name": "Test Restaurant", "owner_id": 1})
    assert response.status_code == 200
