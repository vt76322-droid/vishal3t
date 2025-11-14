# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    """Add custom CLI options for pytest."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome or firefox"
    )

@pytest.fixture
def browser(request):
    """Launch the desired browser with matching WebDriver."""
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    else:  # Default is Chrome
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
