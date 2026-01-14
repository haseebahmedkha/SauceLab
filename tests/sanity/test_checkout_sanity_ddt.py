import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from data.data import checkout_test_data
from utils.logger import LogGen

# ================================
# Test Class: Checkout DDT Tests
# ================================
@pytest.mark.usefixtures("setup")
class TestCheckoutDDT:

    # ================================
    # Test Method: Checkout with Multiple Users
    @pytest.mark.sanity
    @pytest.mark.parametrize("first_name, last_name, postal_code", checkout_test_data)
    def test_checkout_with_multiple_user(self,first_name, last_name, postal_code, setup):
        logger = LogGen().loggen()
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        checkout = CheckoutPage(setup)
        # ================================
        # Test Steps
        logger.info("***** Starting test_checkout_with_multiple_user *****")
        login.goto(BASE_URL)
        logger.info("***** Navigated to BASE_URL *****")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("***** Logged in with valid credentials *****")
        # ================================
        # Add Item to Cart and Checkout
        inventory.add_first_item_to_cart()
        logger.info("***** Added first item to cart *****")
        cart.open_cart()
        logger.info("***** Opened cart *****")
        cart.verify_inventory_item_in_cart("Sauce Labs Backpack")
        logger.info("***** Verified item in cart *****")
        cart.start_checkout()
        logger.info("***** Started checkout *****")
        # ================================
        # Complete Checkout Process
        checkout.enter_userinfo(first_name, last_name, postal_code)
        logger.info("***** Entered user info *****")
        checkout.continue_checkout()
        logger.info("***** Continued checkout *****")
        checkout.finish_checkout()
        logger.info("***** Finished checkout *****")
        # ================================
        # Assert that we are on the order confirmation page
        assert checkout.is_order_completed()
        logger.info("***** Order completed successfully *****")
