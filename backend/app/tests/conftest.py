import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    """FastAPI test client fixture."""
    return TestClient(app)


@pytest.fixture
def sample_user_data():
    """Sample user data for testing."""
    return {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "created_at": "2024-01-01T00:00:00Z",
    }


@pytest.fixture
def mock_database():
    """Mock database connection for testing."""

    class MockDB:
        def __init__(self):
            self.data = {}

        def get(self, key):
            return self.data.get(key)

        def set(self, key, value):
            self.data[key] = value

        def delete(self, key):
            if key in self.data:
                del self.data[key]

        def clear(self):
            self.data.clear()

    db = MockDB()
    yield db
    db.clear()


@pytest.fixture(autouse=True)
def reset_app_state():
    """Reset application state before each test."""
    yield
