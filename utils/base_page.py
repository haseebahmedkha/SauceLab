class BasePage:
    """Small BasePage wrapper around Playwright's Page object for convenience."""

    def __init__(self, page):
        self.page = page

    def goto(self, url: str):
        return self.page.goto(url)

    def click(self, selector: str, **kwargs):
        return self.page.click(selector, **kwargs)

    def fill(self, selector: str, text: str, **kwargs):
        return self.page.fill(selector, text, **kwargs)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def text_content(self, selector: str) -> str:
        return self.page.text_content(selector)

