import time
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = browser.new_page()
        yield page
        page.close()
        browser.close()
