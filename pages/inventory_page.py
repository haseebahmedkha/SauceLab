from utils.base_page import BasePage


class InventoryPage(BasePage):

    inventory_container = ".inventory_list"
    menu_button = "#react-burger-menu-btn"
    logout_link = "#logout_sidebar_link"

    def is_inventory_loaded(self) -> bool:
        return self.page.is_visible(self.inventory_container)

    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)
