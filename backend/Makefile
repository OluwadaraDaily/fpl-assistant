.PHONY: test test-unit test-integration test-e2e test-cov install-deps lint format

# Install dependencies
install-deps:
	pip install -r requirements.txt

# Run all tests
test:
	pytest

# Run unit tests only
test-unit:
	pytest tests/unit/ -m unit

# Run integration tests only
test-integration:
	pytest tests/integration/ -m integration

# Run e2e tests only
test-e2e:
	pytest tests/e2e/ -m e2e

# Run tests with coverage report
test-cov:
	pytest --cov=. --cov-report=html --cov-report=term

# Run tests in parallel
test-parallel:
	pytest -n auto

# Lint code
lint:
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics

# Format code
format:
	black .

# Run pre-commit hooks
pre-commit:
	pre-commit run --all-files