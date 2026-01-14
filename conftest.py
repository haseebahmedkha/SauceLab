import os
import time
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright

# ================================
# PyTest fixture to setup Playwright browser
@pytest.fixture(scope="function")
def setup(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = browser.new_page()
        yield page
        # Take screenshot on test failure
        if request.node.rep_call.failed:
            os.makedirs("Screenshots", exist_ok=True)
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = Path(f"Screenshots/{request.node.name}_{timestamp}.png")
            page.screenshot(path=screenshot_path)
        # Teardown
        page.close()
        context.close()
        browser.close()

# ================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
