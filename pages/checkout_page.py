from utils.base_page import BasePage

# Checkout Page class representing the checkout page
class CheckoutPage(BasePage):
    firstname_input = "#first-name"
    lastname_input = "#last-name"
    postalcode_input = "#postal-code"
    continue_button = "#continue"
    finish_button = "#finish"
    success_message = ".complete-header"

    #  -----------------------
    #  Page Actions
    def enter_userinfo(self, firstname: str, lastname: str, postalcode):
        self.fill(self.firstname_input,firstname)
        self.fill(self.lastname_input,lastname)
        self.fill(self.postalcode_input,postalcode)

    #  -----------------------
    #  Verification Methods
    def continue_checkout(self):
        self.click(self.continue_button)

    #  -----------------------
    #  Page Actions
    def finish_checkout(self):
        self.click(self.finish_button)

    #  -----------------------
    #  Verification Methods
    def is_order_completed(self) -> bool:
        return self.is_visible(self.success_message)