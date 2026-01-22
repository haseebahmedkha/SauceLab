import pytest
import requests
from utils.config import BASE_URL
from utils.logger import LogGen


# ================================
# Test Class: API Health Check
# ================================
class TestAPIHealth:

    # ================================
    # Test Method: Backend is Alive
    @pytest.mark.api
    def test_backend_is_alive(self):
        logger = LogGen().loggen()
        logger.info("***** Starting test_backend_is_alive *****")
         # Send a GET request to the BASE_URL
        response = requests.get(BASE_URL)
        logger.info(f"Received response with status code: {response.status_code}")
        assert response.status_code == 200
        logger.info("***** Backend is alive and responding with status code 200 *****")