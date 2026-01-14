import pytest
from charset_normalizer.md import getLogger
from playwright.sync_api import sync_playwright
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from utils.logger import LogGen
from data.data import test_data_for_login, negative_login_data

# ================================
# Test Class: Login Page Tests
# ================================
@pytest.mark.usefixtures("setup")
class TestLoginPage:

    # ================================
    # Test Method: Valid Login Test
    @pytest.mark.smoke
    def test_valid_login(self,setup):
        logger = LogGen().loggen()
        logger.info("***** Starting test_valid_login *****")
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        login.goto(BASE_URL)
        login.login(VALID_USER, VALID_PASSWORD)
        # assert "inventory" in setup.url
        logger.info("***** Login attempted *****")
        assert inventory.is_inventory_loaded()
        inventory.logout()
        assert "saucedemo" in setup.url
        logger.info("***** test_valid_login completed *****")

    # ================================
    # Test Method: Data-Driven Login Test
    @pytest.mark.parametrize("username,password",test_data_for_login)
    def test_login_ddt(self,username,password,setup):
        logger = LogGen().loggen()
        logger.info("***** Starting test_valid_login *****")
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        login.goto(BASE_URL)
        login.login(username, password)
        # assert "inventory" in setup.url
        logger.info("***** Login attempted *****")
        assert inventory.is_inventory_loaded()
        inventory.logout()
        assert "saucedemo" in setup.url
        logger.info("***** test_valid_login completed *****")

    # ================================
    # Test Method: Invalid Login Test
    @pytest.mark.parametrize("username,password",negative_login_data)
    def test_invalid_login_ddt(self,username,password,setup):
        logger = LogGen().loggen()
        logger.info("***** Starting test_valid_login *****")
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        login.goto(BASE_URL)
        login.login(username, password)
        # assert "inventory" in setup.url
        logger.info("***** Login attempted *****")
        assert inventory.is_inventory_loaded()
        inventory.logout()
        assert "saucedemo" in setup.url
        logger.info("***** test_valid_login completed *****")


