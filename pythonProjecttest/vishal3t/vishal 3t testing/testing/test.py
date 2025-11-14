from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage

import pytest
def test_status_update(browser):
    # Step 1: Login
    login = Login(browser)
    login.load("https://3tstg.csdevhub.com/")
    login.login("niharika@cssoftsolutions.com", "Test@123#")
    print("✅ Logged in successfully")