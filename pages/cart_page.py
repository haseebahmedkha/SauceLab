from utils.base_page import BasePage

# Cart Page class representing the shopping cart page
class CartPage(BasePage):

    # Locators
    cart_icon = ".shopping_cart_link"
    checkout_button = "#checkout"
    inventory_item_name = ".inventory_item_name"

    # Actions
    def open_cart(self):
        self.click(self.cart_icon)

    #  -----------------------
    #  Page Actions
    def start_checkout(self):
        self.click(self.checkout_button)

    #  -----------------------
    #  Verification Methods
    def verify_inventory_item_in_cart(self, item_name: str) -> bool:
        items = self.page.query_selector_all(self.inventory_item_name)
        for item in items:
            if item.inner_text() == item_name:
                return True
        return False

        

