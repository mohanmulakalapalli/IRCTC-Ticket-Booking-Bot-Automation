from pages.login_page import LoginPage
from configurations.test_data import URL_Login, username, password
from tests.conftest import driver
from utilities.customLogger import LogGen
import time
import os
import pytest


@pytest.mark.login
def test_login(driver):
    driver = driver
    screenshots_dir = "report/screenshots"
    logger = LogGen.loggen()  # Logger
    os.makedirs(screenshots_dir, exist_ok=True)  # Ensure the directory exists
    logger.info("******* Starting test_login **********")
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
    assert "Welcome" in driver.page_source or driver.title
    print("Login successful")

    SearchPage = login_page.issearch_page_redirected()
    if SearchPage == True:
        screenshot_path = os.path.join(screenshots_dir, "TL_login_result.png")
        driver.save_screenshot(screenshot_path)
        print(f"Successfull Search page redirected Screenshot saved at: {screenshot_path}")
        logger.info("Search page redirected successfully")
        driver.close()
        assert True
    else:
        print("Search page not redirected")
        logger.error("Search page not redirected")
        # Take screenshot of the error
        screenshot_path = os.path.join(screenshots_dir, "TL_login_error.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        driver.close()
        assert False
    # Close the driver
    driver.quit()
    # Log the end of the test   

    logger.info("******* Ending test_login **********")