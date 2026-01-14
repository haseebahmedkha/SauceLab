import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from utils.logger import LogGen

# ================================
# Test Class: Checkout Flow
# ================================
@pytest.mark.usefixtures("setup")
class TestCheckout:

    # ================================
    # Test Method: Complete Checkout Flow
    @pytest.mark.regression
    def test_complete_checkout_flow(self,setup):
        logger = LogGen().loggen()
        login = LoginPage(setup)
        cart = CartPage(setup)
        checkout = CheckoutPage(setup)
        inventory = InventoryPage(setup)
        # ================================
        # Test Steps
        # ================================
        login.goto(BASE_URL)
        logger.info("Navigated to BASE_URL")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("Logged in with valid credentials")
        # ================================
        # Add Item to Cart and Checkout
        # ================================
        inventory.add_first_item_to_cart()
        logger.info("Added first item to cart")
        cart.open_cart()
        logger.info("Opened cart")
        cart.start_checkout()
        logger.info("Started checkout")
        checkout.enter_userinfo("Haseeb","Khan","12345")
        logger.info("Entered user info")
        # setup.pause()
        # ================================
        # Complete Checkout Process
        checkout.continue_checkout()
        logger.info("Continued checkout")
        checkout.finish_checkout()
        logger.info("Finished checkout")
        # ================================
        # Assert that we are on the order confirmation page
        assert checkout.is_order_completed()
        logger.info("Order completed successfully")




