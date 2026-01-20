import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from utils.logger import LogGen


@pytest.mark.usefixtures("setup")
@pytest.mark.e2e
class TestPurchaseJourney:

    @pytest.mark.critical
    def test_successful_purchase_journey(self,setup):
        logger = LogGen().loggen()
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        checkout = CheckoutPage(setup)
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
        assert inventory.get_cart_count() == "1"
        logger.info("Verified cart count is 1")
        cart.open_cart()
        logger.info("Opened cart")
        cart.start_checkout()
        logger.info("Started checkout")
        # ================================
        # Complete Checkout Process
        checkout.enter_userinfo("Alice","Smith","67890")
        logger.info("Entered user info")
        checkout.continue_checkout()
        logger.info("Continued checkout")
        assert checkout.is_order_summary_displayed()
        logger.info("Verified order summary is displayed")
        checkout.finish_checkout()
        logger.info("Finished checkout")
        # ================================
        # Assert that we are on the order confirmation page
        assert checkout.is_order_completed()
        logger.info("Order completed successfully")


