from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://3tstg.csdevhub.com/"

    email_input = (By.XPATH, '//*[@id="email"]')
    password_input = (By.XPATH, '//*[@id="password"]')
    submit_button = (By.XPATH, '//*[@id="submit-btn"]')

    def go_to_login(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.safe_type(self.email_input, email)
        self.safe_type(self.password_input, password)
        self.safe_click(self.submit_button)
