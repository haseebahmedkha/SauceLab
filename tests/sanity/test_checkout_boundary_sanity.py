import pytest
from utils.logger import LogGen
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.usefixtures("setup")
class TestCheckoutBoundarySanity:
    # ================================
    # Test Method: Checkout with Invalid ZIP (Letters)
    @pytest.mark.sanity
    @pytest.mark.boundary
    def test_checkout_with_invalid_zip_letter(self,setup):

        logger = LogGen.loggen()
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        checkout = CheckoutPage(setup)
        # ================================
        # Test Steps

        logger.info("***** Starting test_checkout_with_invalid_zip_letter *****")
        login.goto(BASE_URL)
        logger.info("***** Navigated to BASE_URL *****")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("***** Logged in with valid credentials *****")
        # ================================

        inventory.add_first_item_to_cart()
        logger.info("***** Added first item to cart *****")
        cart.open_cart()
        logger.info("***** Opened cart *****")
        cart.verify_inventory_item_in_cart("Sauce Labs Backpack")
        logger.info("***** Verified item in cart *****")
        cart.start_checkout()
        logger.info("***** Started checkout *****")
        # ================================
        checkout.enter_userinfo("Alice","Smith","ABCDE")  # Invalid postal code
        logger.info("***** Entered user info with invalid postal code *****")
        checkout.continue_checkout()
        logger.info("***** Continued checkout *****")
        # ================================
        xpath = "xpath=//h3[@data-test='error']"
        # ================================
        # Boundary Validation Assertion
        assert checkout.is_error_displayed(xpath)
        logger.info("***** Error displayed for invalid postal code *****")


    @pytest.mark.boundary
    def test_checkout_with_short_zip(self,setup):
        logger = LogGen.loggen()
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        checkout = CheckoutPage(setup)
        # ================================
        # Test Steps

        logger.info("***** Starting test_checkout_with_short_zip *****")
        login.goto(BASE_URL)
        logger.info("***** Navigated to BASE_URL *****")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("***** Logged in with valid credentials *****")
        # ================================

        inventory.add_first_item_to_cart()
        logger.info("***** Added first item to cart *****")
        cart.open_cart()
        logger.info("***** Opened cart *****")
        cart.verify_inventory_item_in_cart("Sauce Labs Backpack")
        logger.info("***** Verified item in cart *****")
        cart.start_checkout()
        logger.info("***** Started checkout *****")
        # ================================
        checkout.enter_userinfo("Bob", "Johnson", "12")  # Short postal code
        logger.info("***** Entered user info with short postal code *****")
        checkout.continue_checkout()
        logger.info("***** Continued checkout *****")
        # ================================
        xpath = "xpath=//h3[@data-test='error']"
        # ================================
        # Boundary Validation Assertion
        assert checkout.is_error_displayed(xpath)
        logger.info("***** Error displayed for short postal code *****")

    @pytest.mark.boundary
    def test_checkout_with_single_char_firstname(self,setup):
        logger = LogGen.loggen()
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        checkout = CheckoutPage(setup)
        # ================================
        # Test Steps

        logger.info("***** Starting test_checkout_with_single_char_firstname *****")
        login.goto(BASE_URL)
        logger.info("***** Navigated to BASE_URL *****")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("***** Logged in with valid credentials *****")
        # ================================

        inventory.add_first_item_to_cart()
        logger.info("***** Added first item to cart *****")
        cart.open_cart()
        logger.info("***** Opened cart *****")
        cart.verify_inventory_item_in_cart("Sauce Labs Backpack")
        logger.info("***** Verified item in cart *****")
        cart.start_checkout()
        logger.info("***** Started checkout *****")
        # ================================
        checkout.enter_userinfo("A", "Williams", "12345")  # Single character first name
        logger.info("***** Entered user info with single character first name *****")
        checkout.continue_checkout()
        logger.info("***** Continued checkout *****")
        # ================================
        # Assert that we are on the next checkout step
        assert checkout.is_step_two_displayed()
        logger.info("***** Successfully proceeded to overview page with single character first name *****")


