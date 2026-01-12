from utils.base_page import BasePage


class InventoryPage(BasePage):

    inventory_container = ".inventory_list"
    menu_button = "#react-burger-menu-btn"
    logout_link = "#logout_sidebar_link"
    add_to_cart_button = ".btn_inventory"

    def is_inventory_loaded(self) -> bool:
        return self.page.is_visible(self.inventory_container)

    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)

    def add_first_item_to_cart(self):
        self.click(self.add_to_cart_button)
