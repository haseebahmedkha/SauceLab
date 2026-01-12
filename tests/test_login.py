import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD

class Test_loginpage:

    def test_valid_login(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False, slow_mo=500)
            page = browser.new_page()
            login = LoginPage(page)
            login.goto(BASE_URL)
            login.login(VALID_USER, VALID_PASSWORD)
            assert "inventory" in page.url
            page.close()
            browser.close()







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

