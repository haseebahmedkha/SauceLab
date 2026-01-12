from utils.base_page import BasePage


class CheckoutPage(BasePage):
    firstname_input = "#first-name"
    lastname_input = "#last-name"
    postalcode_input = "#postal-code"
    continue_button = "#continue"
    finish_button = "#finish"
    success_message = ".complete-header"

    def enter_userinfo(self, firstname: str, lastname: str, postalcode):
        self.fill(self.firstname_input,firstname)
        self.fill(self.lastname_input,lastname)
        self.fill(self.postalcode_input,postalcode)

    def continue_checkout(self):
        self.click(self.continue_button)

    def finish_checkout(self):
        self.click(self.finish_button)

    def is_order_completed(self) -> bool:
        return self.is_visible(self.success_message)