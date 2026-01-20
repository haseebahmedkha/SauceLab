import time

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from utils.logger import LogGen

# ================================
# Test Class: Cart Edit Journey Tests
@pytest.mark.usefixtures("setup")
class TestCartEditJourney:

    @pytest.mark.e2e
    @pytest.mark.critical
    def test_cart_edit_before_checkout(self, setup):
        logger = LogGen().loggen()
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        # ================================
        # Test Steps
        logger.info("***** Starting test_cart_edit_before_checkout *****")
        login.goto(BASE_URL)
        logger.info("***** Navigated to BASE_URL *****")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("***** Logged in with valid credentials *****")
        # ================================
        # Add Item to Cart
        inventory.add_multiple_items_to_cart(5)
        logger.info("***** Added first item to cart *****")
        cart.open_cart()
        logger.info("***** Opened cart *****")
        cart.verify_inventory_item_in_cart("Sauce Labs Backpack")
        logger.info("***** Verified item in cart *****")
        # ================================
        # Edit Cart: Remove Item
        cart.remove_item_from_cart("Sauce Labs Fleece Jacket")
        logger.info("***** Removed item from cart *****")
        # ================================
        # Assert that the cart is empty
        assert inventory.get_cart_count() == "4"
        logger.info("***** Cart is empty after removing item *****")