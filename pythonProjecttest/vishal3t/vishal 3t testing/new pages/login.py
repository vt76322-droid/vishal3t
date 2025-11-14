# base_page.py
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def safe_send_keys(self, locator, value, retries=3):
        for _ in range(retries):
            try:
                field = self.wait.until(EC.element_to_be_clickable(locator))
                field.clear()
                field.send_keys(value)
                return
            except StaleElementReferenceException:
                time.sleep(1)

    def safe_click(self, locator, retries=3):
        for _ in range(retries):
            try:
                button = self.wait.until(EC.element_to_be_clickable(locator))
                button.click()
                return
            except StaleElementReferenceException:
                time.sleep(1)
