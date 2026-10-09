
"""
Tests for the Smart Problem Resolution Agent.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_resolve_endpoint_returns_expected_fields():
    response = client.post(
        "/resolve",
        json={
            "problem_description": (
                "The Wi-Fi in the computer lab is not working."
            )
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert "category" in data
    assert "priority" in data
    assert "suggested_contact" in data
    assert "contact_email" in data
    assert "recommended_action" in data


def test_resolve_endpoint_rejects_short_input():
    response = client.post(
        "/resolve",
        json={"problem_description": "hi"},
    )

    assert response.status_code in (400, 422)
