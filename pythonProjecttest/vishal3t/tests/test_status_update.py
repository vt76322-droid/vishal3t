from selenium import webdriver
from pages.login import LoginPage
from pages.DashboardPage import DashboardPage
from pages.AddStatusPage import AddStatusPage
from pages.NonBillablePage import NonBillablePage
#from pages.FixedHoursPage import FixedHoursPage
from pages.MemoPage import MemoPage
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Login
    login_page = LoginPage(driver)
    login_page.go_to_login()
    login_page.login("vishal-thakur@cssoftsolutions.com", "Vishal@54321")

    # Navigate to Dashboard Status
    dashboard = DashboardPage(driver)
    dashboard.go_to_status()

    # Add Status
    add_status = AddStatusPage(driver)
    add_status.open_add_status_modal()
    add_status.select_project("Heller")
    add_status.select_module("Heller July 2025 Design")

    # Non-billable
    non_billable = NonBillablePage(driver)
    non_billable.set_offline_hours(hours=2, minutes=10)
    print("[INFO] Non-billable hours set.")

    # Pause before Fixed hours
    #wait_seconds = 15
    #print(f"[INFO] Waiting {wait_seconds} seconds before setting Fixed hours...")
    #time.sleep(wait_seconds)

    # Fixed hours
   # fixed_hours = FixedHoursPage(driver)
    #fixed_hours.set_fixed_hours(hours=2, minutes=30)
    #print("[INFO] Fixed hours set.")

    # Add memo
    memo_page = MemoPage(driver)
    memo_page.enter_memo("This is a non-billable memo for Vishal")
    print("[INFO] Memo added.")

    time.sleep(5)

finally:
    driver.quit()
