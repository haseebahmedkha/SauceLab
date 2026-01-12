from utils.base_page import BasePage


class LoginPage(BasePage):
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"

    def login(self, username: str, password: str):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)

