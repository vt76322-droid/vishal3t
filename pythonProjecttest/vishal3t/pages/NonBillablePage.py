from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from pages.base_page import BasePage

class NonBillablePage(BasePage):
    # --- Locators ---
    OFFLINE_HOURS_INPUT = (By.ID, "offlineHoursupdate")

    # --- Methods ---
    def set_offline_hours(self, hours=2, minutes=10 , timeout=15):
        """
        Sets offline hours and minutes using the clockpicker associated with the input.
        """
        try:
            # Scroll input into view and click
            elem = self.wait.until(EC.element_to_be_clickable(self.OFFLINE_HOURS_INPUT))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
            elem.click()

            # Wait for the visible clockpicker
            clockpicker = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class,'clockpicker') and not(contains(@style,'display: none'))]")
                )
            )

            # Select hours
            hour_elem = clockpicker.find_element(
                By.XPATH, f".//div[contains(@class,'clockpicker-hours')]//div[text()='{hours}']"
            )
            hour_elem.click()

            # Select minutes
            minute_elem = clockpicker.find_element(
                By.XPATH, f".//div[contains(@class,'clockpicker-minutes')]//div[text()='{minutes}']"
            )
            minute_elem.click()

            print(f"[INFO] Non-billable time set to {hours}h:{minutes}m.")

        except TimeoutException:
            print("[ERROR] Offline hours input or clockpicker not found.")
            self.driver.save_screenshot("offline_hours_error.png")
            raise
        except ElementClickInterceptedException:
            print("[WARN] Click intercepted, using JS click fallback.")
            self.driver.execute_script("arguments[0].click();", elem)

