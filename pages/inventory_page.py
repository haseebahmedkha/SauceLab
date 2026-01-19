from utils.base_page import BasePage

# Inventory Page class representing the inventory page
class InventoryPage(BasePage):

    # Locators
    inventory_container = ".inventory_list"
    menu_button = "#react-burger-menu-btn"
    logout_link = "#logout_sidebar_link"
    add_to_cart_button = ".btn_inventory"

    #  -----------------------
    #  Verification Methods
    def is_inventory_loaded(self) -> bool:
        return self.page.is_visible(self.inventory_container)

    #  -----------------------
    #  Page Actions
    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)

    #  -----------------------
    #  Page Actions
    def add_first_item_to_cart(self):
        self.click(self.add_to_cart_button)

    # -----------------------
    def get_cart_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()

    def add_multiple_items_to_cart(self, count: int):
        buttons = self.page.query_selector_all(self.add_to_cart_button)
        for i in range(min(count, len(buttons))):
            buttons[i].click()

    def remove_first_item_from_cart(self):
        remove_button = self.page.locator(".btn_inventory").filter(has_text="Remove").first
        remove_button.click()

