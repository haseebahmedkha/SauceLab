import time
from pathlib import Path

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.saucedemo.com",
        help="base url for tests",
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")


def pytest_configure(config):
    # Ensure reports directories exist
    Path("reports/screenshots").mkdir(parents=True, exist_ok=True)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # only act on actual test call failures
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page") if hasattr(item, "funcargs") else None
        if page:
            timestamp = int(time.time())
            filename = f"reports/screenshots/{item.name}_{timestamp}.png"
            try:
                # page is a Playwright Page fixture (sync API)
                page.screenshot(path=filename, full_page=True)
                # add a log message so it's easy to find
                if hasattr(rep, "longrepr"):
                    rep.longrepr = f"Screenshot saved to: {filename}\n" + str(rep.longrepr)
                else:
                    rep.longrepr = f"Screenshot saved to: {filename}\n"
            except Exception as exc:  # pragma: no cover - defensive
                print(f"Could not take screenshot for {item.name}: {exc}")
