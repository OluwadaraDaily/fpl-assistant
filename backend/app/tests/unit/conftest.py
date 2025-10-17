import pytest
from unittest.mock import Mock, AsyncMock


@pytest.fixture
def mock_external_api():
    """Mock external API client."""
    mock = Mock()
    mock.get.return_value = {"status": "success", "data": {}}
    mock.post.return_value = {"status": "created", "id": 123}
    return mock


@pytest.fixture
def mock_async_service():
    """Mock async service for unit tests."""
    mock = AsyncMock()
    mock.process.return_value = {"result": "processed"}
    return mock
