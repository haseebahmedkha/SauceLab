import pytest
from charset_normalizer.md import getLogger
from playwright.sync_api import sync_playwright

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from utils.logger import LogGen


@pytest.mark.usefixtures("setup")
class TestLoginPage:


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








# @pytest.mark.smoke
# def test_successful_login(page, base_url):
#     # navigate to the site
#     page.goto(base_url)
#
#     login = LoginPage(page)
#     login.login("standard_user", "secret_sauce")
#
#     # assert that we are on the inventory page by checking a known selector
#     assert page.is_visible(".inventory_list")

