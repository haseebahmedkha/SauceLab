from utils.base_page import BasePage

# Cart Page class representing the shopping cart page
class CartPage(BasePage):

    # Locators
    cart_icon = ".shopping_cart_link"
    checkout_button = "#checkout"
    inventory_item_name = ".inventory_item_name"
    remove_button = "xpath=//button[@id='remove-sauce-labs-backpack']"

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

    def remove_item_from_cart(self,item_name: str):
        for item in self.page.query_selector_all(self.inventory_item_name):
            if item.inner_text() == item_name:
                remove_button = self.page.locator(self.remove_button).filter(has_text="Remove")
                remove_button.click()



        

