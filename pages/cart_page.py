from utils.base_page import BasePage


class CartPage(BasePage):

    cart_icon = ".shopping_cart_link"
    checkout_button = "#checkout"

    def open_cart(self):
        self.click(self.cart_icon)

    def start_checkout(self):
        self.click(self.checkout_button)

        

