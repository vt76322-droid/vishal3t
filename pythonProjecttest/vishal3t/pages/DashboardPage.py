from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    dashboard_status_link = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div[3]/div[2]/div[2]/ul/li[2]/a/span')

    def go_to_status(self):
        self.safe_click(self.dashboard_status_link)
