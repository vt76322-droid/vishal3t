import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:
    def __init__(self, driver, wait_time=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def safe_click(self, locator, retries=2):
        for _ in range(retries):
            try:
                elem = self.wait.until(EC.element_to_be_clickable(locator))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
                time.sleep(6)
                try:
                    elem.click()
                except:
                    self.driver.execute_script("arguments[0].click();", elem)
                return
            except StaleElementReferenceException:
                time.sleep(6)
        raise Exception(f"Failed to click element {locator}")

    def safe_type(self, locator, text, retries=2):
        for _ in range(retries):
            try:
                elem = self.wait.until(EC.visibility_of_element_located(locator))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
                elem.clear()
                elem.send_keys(text)
                return
            except StaleElementReferenceException:
                time.sleep(6)
        raise Exception(f"Failed to type in element {locator}")

    def safe_find(self, locator, retries=2):
        for _ in range(retries):
            try:
                return self.wait.until(EC.visibility_of_element_located(locator))
            except StaleElementReferenceException:
                time.sleep(6)
        raise Exception(f"Failed to find element {locator}")
