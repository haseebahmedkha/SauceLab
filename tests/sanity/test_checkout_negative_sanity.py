import pytest
from data.data import negative_checkout_data
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import LogGen
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD


# ================================
# Test Class: Checkout Negative Sanity Tests
# ================================
@pytest.mark.usefixtures("setup")
class TestCheckoutNegativeSanityErrorMessage:

    # ================================
    # Test Method: Checkout with Invalid Data
    @pytest.mark.negative
    @pytest.mark.parametrize("first_name, last_name, postal_code,error_message",negative_checkout_data)
    def test_checkout_with_invalid_data_error_message(self,first_name,last_name,postal_code,error_message,setup):
        page = setup
        logger = LogGen().loggen()
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        checkout = CheckoutPage(setup)
        # ================================
        # Test Steps
        xpath = "xpath=//h3[@data-test='error']"
        logger.info("***** Starting test_checkout_with_invalid_data_error_message *****")
        login.goto(BASE_URL)
        logger.info("***** Navigated to BASE_URL *****")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("***** Logged in with valid credentials *****")
        inventory.add_first_item_to_cart()
        logger.info("***** Added first item to cart *****")
        cart.open_cart()
        logger.info("***** Opened cart *****")
        cart.start_checkout()
        logger.info("***** Started checkout *****")
        checkout.enter_userinfo(first_name, last_name, postal_code)
        logger.info("***** Entered user info *****")
        checkout.continue_checkout()
        logger.info("***** Continued checkout *****")
        # assert page.locator("xpath=//h3[@data-test='error']").inner_text() == error_message
        assert checkout.return_error_message(xpath) == error_message
        logger.info("***** Verified error message *****")
        logger.info("***** test_checkout_with_invalid_data_error_message completed *****")

