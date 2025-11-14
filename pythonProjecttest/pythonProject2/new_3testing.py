from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

try:
    print("Opening the website...")
    driver.get('https://3tstaging.csdevhub.com/')  # Replace with your actual URL

    wait = WebDriverWait(driver, 30)

    print("Waiting for email field...")
    email_element = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    email_element.send_keys('abhithakur@csgroupchd.com')

    print("Waiting for password field...")
    password_element = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_element.send_keys('Test@123#')

    print("Waiting for 'Remember Me' checkbox...")
    remember_me_element = wait.until(EC.element_to_be_clickable((By.ID, 'RememberMe')))
    remember_me_element.click()

    print("Waiting for login button...")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Login")]')))
    login_button.click()

    print("Waiting for 'Add Status' button...")
    add_status_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Add Status")]')))
    add_status_button.click()

    print("Waiting for 'Select Project' dropdown...")
    project_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "select-project")]')))
    project_dropdown.click()

    time.sleep(1)  # Consider replacing with explicit wait if possible

    print("Entering project name 'LICC Infobase'...")
    project_search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search..."]')))
    project_search_box.send_keys('LICC Infobase')

    time.sleep(1)

    print("Selecting project 'LICC Infobase'...")
    select_project = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "LICC Infobase")]')))
    select_project.click()

    print("Waiting for 'Select Module' dropdown...")
    module_dropdown = wait.until(EC.element_to_be_clickable((By.ID, 'BuildHour_ModuleName')))
    module_dropdown.click()

    time.sleep(1)

    print("Selecting module 'IFL 540'...")
    module_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//option[text()="IFL 540"]')))
    module_option.click()

    print("Waiting for 'Profile' dropdown...")
    profile_dropdown = wait.until(EC.element_to_be_clickable((By.ID, 'BuildHour_ProfileId')))
    profile_dropdown.click()

    time.sleep(1)

    print("Selecting profile 'AA'...")
    profile_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//option[text()="AA"]')))
    profile_option.click()

    print("Selecting the date...")
    calendar_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="calendar-icon"]')))
    calendar_icon.click()

    current_date = wait.until(EC.element_to_be_clickable((By.XPATH, '//td[contains(@class, "today")]')))
    current_date.click()

    print("Entering non-billable hours...")
    non_billable_hours = wait.until(EC.presence_of_element_located((By.ID, 'BuildHour_OfflineHours')))
    non_billable_hours.clear()
    driver.execute_script("arguments[0].value = '08:30';", non_billable_hours)

    print("Entering memo text...")
    memo_field = wait.until(EC.presence_of_element_located((By.ID, 'BuildHour_Memo')))
    memo_field.clear()
    memo_field.send_keys('test')

    print("Submitting and sending status mail...")
    submit_mail_button = wait.until(EC.element_to_be_clickable((By.ID, 'submitMail')))
    submit_mail_button.click()

    print("Scrolling to 'My Status'...")
    my_status = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "My Status")]')))
    driver.execute_script("arguments[0].scrollIntoView(true);", my_status)
    driver.execute_script("arguments[0].click();", my_status)

    time.sleep(40)  # Allow time to observe the result

finally:
    driver.quit()  # Ensure the driver is closed properly
