from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class MemoPage(BasePage):
    # --- Locators ---
    MEMO_INPUT = (By.XPATH, "//*[@id='inputState']")

    # --- Methods ---
    def enter_memo(self, text):
        """
        Enters the given text into the Memo input field.
        """
        try:
            memo_elem = self.wait.until(
                EC.element_to_be_clickable(self.MEMO_INPUT)
            )
            memo_elem.clear()
            memo_elem.send_keys(text)
            print(f"[INFO] Memo entered: {text}")
        except TimeoutException:
            print("[ERROR] Memo input not found or not clickable.")
            self.driver.save_screenshot("memo_input_error.png")
            raise
