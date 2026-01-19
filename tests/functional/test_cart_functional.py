import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD
from utils.logger import LogGen


# ================================
# Test Class: Cart Functional Tests
# ================================
@pytest.mark.usefixtures("setup")
class TestCartFunctional:

    # ================================
    # Test Method: Add Single Item to Cart
    @pytest.mark.functional
    def test_add_single_item_to_cart(self, setup):
        logger = LogGen().loggen()
        logger.info("***** Starting test_add_single_item_to_cart *****")
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        # Test Steps
        login.goto(BASE_URL)
        logger.info("Navigated to BASE_URL")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("Logged in with valid credentials")
        inventory.add_first_item_to_cart()
        logger.info("Added first item to cart")
        # Verify Cart Count
        assert inventory.get_cart_count() == "1"
        logger.info("Cart count is correct")

    # ================================
    # Test Method: Add Multiple Items to Cart
    @pytest.mark.functional
    def test_multiple_item_to_cart(self,setup):
        logger = LogGen().loggen()
        logger.info("***** Starting test_multiple_item_to_cart *****")
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        # Test Steps
        login.goto(BASE_URL)
        logger.info("Navigated to BASE_URL")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("Logged in with valid credentials")
        inventory.add_multiple_items_to_cart(3)
        logger.info("Added items to cart")
        assert inventory.get_cart_count() == "3"
        logger.info("Cart count is correct")

    @pytest.mark.functional
    def test_remove_item_from_cart(self,setup):
        logger = LogGen().loggen()
        logger.info("***** Starting test_remove_item_from_cart *****")
        login = LoginPage(setup)
        inventory = InventoryPage(setup)
        cart = CartPage(setup)
        # Test Steps
        login.goto(BASE_URL)
        logger.info("Navigated to BASE_URL")
        login.login(VALID_USER, VALID_PASSWORD)
        logger.info("Logged in with valid credentials")
        inventory.add_multiple_items_to_cart(2)
        logger.info("Added items to cart")
        assert inventory.get_cart_count() == "2"
        logger.info("Cart count is correct")
        inventory.remove_first_item_from_cart()
        logger.info("Removed first item from cart")
        assert inventory.get_cart_count() == "1"
        logger.info("Cart count after removal is correct")


