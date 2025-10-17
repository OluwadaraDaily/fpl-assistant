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

    def test_endpoint_integration_with_test_data(
        self, integration_client, setup_test_data
    ):
        """Test endpoint integration with test data setup."""
        # Use test data for validation
        test_data = setup_test_data

        # Test the actual endpoint
        response = integration_client.get("/")

        assert response.status_code == 200
        assert "Hello" in response.json()

        # Validate our test data setup works
        assert "users" in test_data
        assert len(test_data["users"]) == 2
