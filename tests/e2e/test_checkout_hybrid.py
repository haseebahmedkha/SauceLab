import pytest,requests
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from utils.logger import LogGen

# ================================
@pytest.mark.usefixtures("setup")
class TestCheckoutHybrid:
    @pytest.mark.e2e
    @pytest.mark.hybrid
    def test_checkout_hybrid(self, setup):
        logger = LogGen().loggen()
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        # ================================
        # Test Steps
        login.goto(BASE_URL)
        logger.info("Navigated to BASE_URL")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("Logged in with valid credentials")
        inventory.add_first_item_to_cart()
        # ================================
        response = requests.get(BASE_URL)
        logger.info("Performed backend GET request to BASE_URL")
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        logger.info("Backend GET request successful with status code 200")