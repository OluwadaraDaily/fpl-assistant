import pytest


class TestUserFlows:
    """End-to-end tests for complete user workflows."""

    def test_basic_application_flow(self, e2e_client):
        """Test basic application access and response."""
        response = e2e_client.get("/")

        assert response.status_code == 200

        json_response = response.json()
        assert json_response["Hello"] == "World"

    @pytest.mark.slow
    def test_complete_user_journey(self, e2e_client):
        """Test a complete user journey through the application."""
        # Step 1: Access the application
        home_response = e2e_client.get("/")
        assert home_response.status_code == 200

        # Step 2: Verify application is responsive
        assert home_response.json() == {"Hello": "World"}

        # Add more steps as you build out your API
        # e.g., user registration, login, data operations

    @pytest.mark.e2e
    def test_api_error_handling(self, e2e_client):
        """Test that the API handles errors gracefully in e2e context."""
        response = e2e_client.get("/nonexistent-endpoint")

        assert response.status_code == 404
        # Verify error response structure
        assert "detail" in response.json()
