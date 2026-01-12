import pytest
from playwright.sync_api import sync_playwright

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD

class Test_loginpage:



    @pytest.mark.smoke
    @pytest.mark.usefixtures("setup")
    def test_valid_login(self,setup):
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        login.goto(BASE_URL)
        login.login(VALID_USER, VALID_PASSWORD)
        # assert "inventory" in setup.url
        assert inventory.is_inventory_loaded()
        inventory.logout()
        assert "saucedemo" in setup.url








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

