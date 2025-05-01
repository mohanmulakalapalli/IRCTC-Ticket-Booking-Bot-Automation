from pages.login_page import LoginPage
from pages.test_data import URL_Login, username, password
from tests.driver_setup import driver_setup
import time
import os
import pytest

def test_login(driver_setup):
    driver = driver_setup
    screenshots_dir = "report/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)  # Ensure the directory exists
    driver.get(URL_Login)
    driver.maximize_window()
    # Take screenshot login page
    screenshot_path = os.path.join(screenshots_dir, "TL_login_page.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")
    # Login
    login_page = LoginPage(driver)
    captcha_text = login_page.get_captcha_text()
    login_page.login(username, password, captcha_text)
    time.sleep(2)  # Wait for the alert to appear
    # Accept alert
    login_page.accept_alert()
    screenshot_path = os.path.join(screenshots_dir, "TL_login_result.png")
    driver.save_screenshot(screenshot_path)
    print(f"Successfull seaech page redirected Screenshot saved at: {screenshot_path}")

    assert "Welcome" in driver.page_source or driver.title
    print("Login successful")