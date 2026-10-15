
import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page_returns_success(client):
    response = client.get("/")
    assert response.status_code == 200


def test_health_endpoint_returns_success(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_endpoint_returns_expected_json(client):
    response = client.get("/health")
    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["application"] == "Python Jenkins Deployment App"
