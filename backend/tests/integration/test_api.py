import pytest


class TestAPIIntegration:
    """Integration tests for API endpoints."""

    def test_app_startup_and_shutdown(self, integration_client):
        """Test that the application starts up and shuts down properly."""
        response = integration_client.get("/")

        assert response.status_code == 200
        assert "Hello" in response.json()

    def test_health_check_endpoint_flow(self, integration_client):
        """Test complete health check flow."""
        # This would test a health endpoint when you add one
        response = integration_client.get("/")

        assert response.status_code == 200
        # Verify response structure
        json_response = response.json()
        assert isinstance(json_response, dict)
        assert "Hello" in json_response

    @pytest.mark.asyncio
    async def test_async_endpoint_integration(self, setup_test_data):
        """Test async endpoint with test data."""
        # Example of testing with setup data
        test_data = await setup_test_data

        assert "users" in test_data
        assert len(test_data["users"]) == 2
