import pytest


class TestMainEndpoints:
    """Unit tests for main application endpoints."""

    def test_read_root_returns_hello_world(self, client):
        """Test that root endpoint returns expected greeting."""
        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}

    def test_read_root_content_type(self, client):
        """Test that root endpoint returns JSON content type."""
        response = client.get("/")

        assert response.headers["content-type"] == "application/json"

    @pytest.mark.parametrize(
        "invalid_path", ["/invalid", "/does-not-exist", "/api/unknown"]
    )
    def test_invalid_endpoints_return_404(self, client, invalid_path):
        """Test that invalid endpoints return 404."""
        response = client.get(invalid_path)

        assert response.status_code == 404
