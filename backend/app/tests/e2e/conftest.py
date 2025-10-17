import pytest
import subprocess
import time
import requests


@pytest.fixture(scope="session")
def server_url():
    """Base URL for the running server."""
    return "http://localhost:8000"


@pytest.fixture(scope="session")
def start_server():
    """Start the FastAPI server for e2e tests."""
    process = subprocess.Popen(
        ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"],
        cwd="/Users/mac/Desktop/projects/side-projects/fpl-assistant/backend",
    )

    # Wait for server to start
    for _ in range(30):
        try:
            response = requests.get("http://localhost:8000/")
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    else:
        process.kill()
        raise RuntimeError("Server failed to start")

    yield process

    # Cleanup
    process.terminate()
    process.wait()


@pytest.fixture
def e2e_client(start_server, server_url):
    """HTTP client for e2e tests."""

    class E2EClient:
        def __init__(self, base_url):
            self.base_url = base_url

        def get(self, path):
            return requests.get(f"{self.base_url}{path}")

        def post(self, path, json=None, data=None):
            return requests.post(f"{self.base_url}{path}", json=json, data=data)

        def put(self, path, json=None, data=None):
            return requests.put(f"{self.base_url}{path}", json=json, data=data)

        def delete(self, path):
            return requests.delete(f"{self.base_url}{path}")

    return E2EClient(server_url)
