import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def valid_post_payload():
    """Fixture that returns sample data for creating a post"""
    return {
        "title": "QA Automation Test",
        "body": "This is a test post created from my API automation repo",
        "userId": 1
    }


def test_get_posts_returns_200():
    """Test that GET /posts endpoint returns 200 OK"""
    response = requests.get(f"{BASE_URL}/posts")

    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    print("GET /posts returned 200 OK")


def test_get_single_post_returns_200():
    """Test that GET /posts/1 returns 200 OK and correct data"""
    response = requests.get(f"{BASE_URL}/posts/1")

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert data["id"] == 1
    print("GET /posts/1 returned 200 OK")


def test_create_post_returns_201(valid_post_payload):
    """Test that POST /posts returns 201 Created"""
    response = requests.post(f"{BASE_URL}/posts", json=valid_post_payload)

    assert response.status_code == 201, f"Expected 201, but got {response.status_code}"
    print("POST /posts returned 201 Created")