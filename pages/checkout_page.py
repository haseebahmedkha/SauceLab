from utils.base_page import BasePage

# Checkout Page class representing the checkout page
class CheckoutPage(BasePage):
    firstname_input = "#first-name"
    lastname_input = "#last-name"
    postalcode_input = "#postal-code"
    continue_button = "#continue"
    finish_button = "#finish"
    success_message = ".complete-header"
    summary_info = ".summary_info"
    cancel_button = "#cancel"


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

    #  -----------------------
    #  Verification Methods
    def return_error_message(self,xpath)-> str:
        return self.page.locator(xpath).inner_text()

    #  -----------------------
    #  Verification Methods
    def is_error_displayed(self,xpath)-> str:
        return self.page.locator(xpath).is_visible()

    #  -----------------------
    #  Verification Methods
    def is_step_two_displayed(self) -> bool:
        return "checkout-step-two" in self.page.url

    def is_order_summary_displayed(self) -> bool:
        return self.is_visible(self.summary_info)

    def cancel_checkout(self):
        self.page.locator(self.cancel_button).click()
