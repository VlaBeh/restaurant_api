import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_login():
    response = client.post("/auth", json={"username": "test", "password": "test"})
    assert response.status_code == 200


def test_successful_login():
    response = client.post("/auth/login", json={"username": "valid_user", "password": "valid_password"})
    assert response.status_code == 200
    assert "access_token" in response.json()
