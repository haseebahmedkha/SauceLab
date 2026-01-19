
# A simple BasePage class that wraps Playwright's Page object for convenience.
class BasePage:
    """Small BasePage wrapper around Playwright's Page object for convenience."""

    # -----------------------
    #  Initialization
    def __init__(self, page):
        self.page = page

    # -----------------------
    #  Page Actions
    def goto(self, url: str):
        return self.page.goto(url)

    # -----------------------
    #  Page Actions
    def click(self, selector: str, **kwargs):
        return self.page.click(selector, **kwargs)

    # -----------------------
    #  Page Actions
    def fill(self, selector: str, text: str, **kwargs):
        return self.page.fill(selector, text, **kwargs)

    # -----------------------
    #  Verification Methods
    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    # -----------------------
    def text_content(self, selector: str) -> str:
        return self.page.text_content(selector)


    def go_back(self):
        return self.page.go_back()

    def go_forward(self):
        return self.page.go_forward()

