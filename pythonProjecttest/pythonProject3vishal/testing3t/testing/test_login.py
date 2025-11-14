import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

# ✅ fixed import

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("varun-choudhary@cssoftsolutions.com", "Test@123#")
    # Add assertion here (example: check page title or dashboard element)
