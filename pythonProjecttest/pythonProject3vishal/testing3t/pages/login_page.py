# login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    # Locators
    EMAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submit-btn"]')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        """Navigate to the login page."""
        self.driver.get("https://3tstg.csdevhub.com/account/login")

    def set_email(self, email):
        """Enter the email into the email input field."""
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        """Enter the password into the password input field."""
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """Click the login button."""
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def login(self, email, password):
        """Full login flow."""
        self.set_email(email)
        self.set_password(password)
        self.click_login()
