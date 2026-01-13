import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config import BASE_URL, VALID_USER, VALID_PASSWORD


@pytest.mark.usefixtures("setup")
class TestCheckout:

    @pytest.mark.regression
    def test_complete_checkout_flow(self,setup):
        login = LoginPage(setup)
        cart = CartPage(setup)
        checkout = CheckoutPage(setup)
        inventory = InventoryPage(setup)


        login.goto(BASE_URL)
        login.login(VALID_USER, VALID_PASSWORD)

        inventory.add_first_item_to_cart()
        cart.open_cart()
        cart.start_checkout()

        checkout.enter_userinfo("Haseeb","Khan","12345")
        # setup.pause()
        checkout.continue_checkout()
        checkout.finish_checkout()
        assert checkout.is_order_completed()




