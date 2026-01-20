import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from utils.logger import LogGen

# ================================
# Test Class: Checkout Error Recovery
@pytest.mark.usefixtures("setup")
class TestCheckoutErrorRecovery:

    # ================================
    # Test Method: Checkout Error Recovery
    @pytest.mark.e2e
    def test_checkout_error_recovery(self, setup):
        logger = LogGen().loggen()
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        checkout = CheckoutPage(setup)
        # ================================
        # Test Steps
        logger.info("***** Starting test_checkout_error_recovery *****")
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
        # Attempt Checkout with Missing Info to Trigger Error
        checkout.enter_userinfo("", "Doe", "54321")
        checkout.continue_checkout()
        assert checkout.is_error_displayed()# Missing first name
        logger.info("***** Entered incomplete user info to trigger error *****")
        checkout.enter_userinfo("John", "Doe", "54321")
        logger.info("***** Corrected user info *****")
        # ================================
        # Complete Checkout Process After Recovery
        checkout.continue_checkout()
        logger.info("***** Continued checkout after error *****")
        # ================================
        # Assert that we are on the order confirmation page
        assert checkout.is_order_summary_displayed()
        checkout.finish_checkout()
        # ================================
        logger.info("***** Finished checkout *****")
        assert checkout.is_order_completed()
        logger.info("***** Order completed successfully after recovery *****")





