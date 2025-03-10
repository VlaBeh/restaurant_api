import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/auth/login", json={"username": "test", "password": "wrong_password"})
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_successful_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/auth/login", json={"username": "valid_user", "password": "valid_password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
