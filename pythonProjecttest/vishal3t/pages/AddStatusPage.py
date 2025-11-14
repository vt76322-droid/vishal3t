from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from pages.base_page import BasePage

class AddStatusPage(BasePage):
    # --- Locators ---
    ADD_STATUS_BUTTON = (By.XPATH, "//button[contains(., 'Add Status')]")
    PROJECT_INPUT = (By.CSS_SELECTOR, "div.mydropdown input[placeholder='Select Project']")
    PROJECT_OPTION_XPATH = "//ul[@id='threeTSelectUL']//span[normalize-space()='{}']"
    MODULE_DROPDOWN = (By.ID, "moduleDropdown")
    MODULE_OPTION_XPATH = "//ul[contains(@class,'dropdown-menu')]//a[@title='{}']"
    ADD_STATUS_MODAL = (By.ID, "AddStatusModal")

    # --- Methods ---
    def open_add_status_modal(self, timeout=20):
        """
        Opens the 'Add Status' modal using the BasePage wait.
        """
        print("[INFO] Attempting to open 'Add Status' modal...")
        self.driver.save_screenshot("before_add_status.png")
        try:
            # Wait for button to be present and visible
            elem = self.wait.until(lambda d: d.find_element(*self.ADD_STATUS_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)

            # Wait until clickable
            elem = self.wait.until(lambda d: d.find_element(*self.ADD_STATUS_BUTTON).is_enabled() and elem)

            # Click with JS fallback
            try:
                elem.click()
                print("[INFO] 'Add Status' button clicked.")
            except ElementClickInterceptedException:
                print("[WARN] Click intercepted, using JS click.")
                self.driver.execute_script("arguments[0].click();", elem)

            # Wait for modal visibility
            self.wait.until(lambda d: d.find_element(*self.ADD_STATUS_MODAL).is_displayed())
            print("[INFO] 'Add Status' modal is now visible.")

        except TimeoutException:
            print("[ERROR] 'Add Status' button not found or not clickable.")
            self.driver.save_screenshot("add_status_button_error.png")
            raise

    def select_project(self, project_name="Heller", timeout=10):
        """
        Selects a project from the dropdown.
        """
        self.safe_click(self.PROJECT_INPUT)

        option_xpath = self.PROJECT_OPTION_XPATH.format(project_name)
        option = self.wait.until(lambda d: d.find_element(By.XPATH, option_xpath))

        try:
            option.click()
            print(f"[INFO] Project '{project_name}' selected.")
        except ElementClickInterceptedException:
            print("[WARN] Click intercepted, using JS click.")
            self.driver.execute_script("arguments[0].click();", option)

    def select_module(self, module_name="Heller July 2025 Design", timeout=10):
        """
        Selects a module from the dropdown. Skips click if already active.
        """
        dropdown = self.wait.until(lambda d: d.find_element(*self.MODULE_DROPDOWN))
        dropdown.click()

        module_xpath = self.MODULE_OPTION_XPATH.format(module_name)
        option = self.wait.until(lambda d: d.find_element(By.XPATH, module_xpath))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", option)

        if "active" not in option.get_attribute("class"):
            try:
                option.click()
                print(f"[INFO] Module '{module_name}' clicked.")
            except ElementClickInterceptedException:
                print("[WARN] Click intercepted, using JS click.")
                self.driver.execute_script("arguments[0].click();", option)
        else:
            print(f"[INFO] Module '{module_name}' already active, skipping click.")
