import pytest
import asyncio
from fastapi.testclient import TestClient


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
def integration_client():
    """Test client for integration tests with proper setup/teardown."""
    from main import app

    with TestClient(app) as client:
        yield client


@pytest.fixture
def test_database_url():
    """Test database URL for integration tests."""
    return "sqlite:///./test.db"


@pytest.fixture
async def setup_test_data():
    """Setup test data for integration tests."""
    test_data = {
        "users": [
            {"id": 1, "name": "Test User 1", "email": "test1@example.com"},
            {"id": 2, "name": "Test User 2", "email": "test2@example.com"},
        ]
    }

    yield test_data
