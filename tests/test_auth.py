import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Create tables before tests run
    Base.metadata.create_all(bind=engine)
    yield
    # Drop tables after all tests in this module complete (optional)
    Base.metadata.drop_all(bind=engine)


def test_register_and_login_and_refresh():
    # Test user registration
    response = client.post("/auth/register", json={"email": "testuser@example.com", "password": "strongpassword"})
    print(response.json())  # To debug if still failing
    assert response.status_code == 201

    # Test duplicate registration returns error
    response = client.post("/auth/register", json={"email": "testuser@example.com", "password": "strongpassword"})
    assert response.status_code == 400

    # Test login with correct credentials
    response = client.post("/auth/login", json={"email": "testuser@example.com", "password": "strongpassword"})
    assert response.status_code == 200
    tokens = response.json()
    assert "access_token" in tokens and "refresh_token" in tokens

    # Test refresh token usage
    refresh_token = tokens["refresh_token"]
    response = client.post("/auth/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_list_routes():
    routes = [route.path for route in app.routes]
    print("Registered routes:", routes)
    assert "/auth/register" in routes
