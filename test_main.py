import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
ACCOUNT_URL = "https://magento.softwaretestingboard.com/customer/account/"
EMAIL = "hasmik.gev@gmail.com"
PASSWORD = "Has.2024agbu"
NEW_PASSWORD = "Has.2024agbu"


@pytest.fixture(scope='module')
def driver():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.regression
@allure.feature('Login')
@allure.suite('Login Tests')
@allure.title('Invalid Login Test')
@allure.description('Test login functionality with invalid credentials.')
@allure.severity('critical')
def test_invalid_login(driver):
    with allure.step('Open login page'):
        driver.get(LOGIN_URL)

    with allure.step('Enter invalid email'):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("invalidemail@gmail.com")

    with allure.step('Enter invalid password'):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys("invalidpassword")

    with allure.step('Click login button'):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()

    with allure.step('Verify error message'):
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, value='//*[@id="maincontent"]/div[2]/div[2]/div/div/div')
        assert "Please wait and try again later" in error_message.text


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Login')
@allure.suite('Login Tests')
@allure.title('Successful Login Test')
@allure.description('Test successful login with valid credentials.')
@allure.severity('blocker')
def test_login(driver):
    with allure.step('Open login page'):
        driver.get(LOGIN_URL)

    with allure.step('Enter valid email'):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys(EMAIL)

    with allure.step('Enter valid password'):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys(PASSWORD)

    with allure.step('Click login button'):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()

    with allure.step('Verify account page is loaded'):
        time.sleep(3)  # Wait for the page to load
        assert driver.current_url == ACCOUNT_URL


@pytest.mark.regression
@allure.feature('Password Management')
@allure.suite('Password Change Tests')
@allure.title('Incorrect Current Password Test')
@allure.description('Test changing password with an incorrect current password.')
@allure.severity('critical')
def test_change_password_incorrect_current(driver):
    with allure.step('Open account page'):
        driver.get(ACCOUNT_URL)

    with allure.step('Navigate to Change Password page'):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step('Enter incorrect current password'):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys("incorrectpassword")

    with allure.step('Enter new password'):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Confirm new password'):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Click save button'):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step('Verify error message for incorrect password'):
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-error')]")
        assert "The password doesn't match this account." in error_message.text


@pytest.mark.regression
@allure.feature('Password Management')
@allure.suite('Password Change Tests')
@allure.title('Password Mismatch Test')
@allure.description('Test changing password with mismatched new passwords.')
@allure.severity('critical')
def test_change_password_mismatch(driver):
    with allure.step('Open account page'):
        driver.get(ACCOUNT_URL)

    with allure.step('Navigate to Change Password page'):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step('Enter current password'):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step('Enter new password'):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Enter mismatched confirm password'):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys("mismatchedpassword")

    with allure.step('Click save button'):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step('Verify password mismatch error'):
        time.sleep(3)
        error_message = driver.find_element(By.ID, "password-confirmation-error")
        assert "Please enter the same value again." in error_message.text


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Password Management')
@allure.suite('Password Change Tests')
@allure.title('Successful Password Change Test')
@allure.description('Test changing password successfully with correct inputs.')
@allure.severity('blocker')
def test_change_password(driver):
    with allure.step('Open account page'):
        driver.get(ACCOUNT_URL)

    with allure.step('Navigate to Change Password page'):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step('Enter current password'):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step('Enter new password'):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Confirm new password'):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(NEW_PASSWORD)

    with allure.step('Click save button'):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step('Verify success message'):
        success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'message-success')]")
        assert "You saved the account information." in success_message.text
