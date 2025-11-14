from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FixedHoursPage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.FIXED_HOURS_INPUT = (By.ID, "fixedHoursupdate")

    def set_fixed_hours(self, hours=2, minutes=30):
        # Step 1: Click input
        input_elem = self.wait.until(EC.element_to_be_clickable(self.FIXED_HOURS_INPUT))
        input_elem.click()

        # Step 2: Wait for hours dial visible
        hours_xpath = f"//div[contains(@class,'clockpicker-dial') and contains(@class,'clockpicker-hours')]//div[text()='{hours}']"
        hour_elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, hours_xpath)))
        hour_elem.click()

        # Step 3: Wait for minutes dial visible
        minutes_xpath = f"//div[contains(@class,'clockpicker-dial') and contains(@class,'clockpicker-minutes')]//div[text()='{minutes}']"
        minute_elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, minutes_xpath)))
        minute_elem.click()

        print(f"[INFO] Fixed hours set to {hours}:{minutes}")
