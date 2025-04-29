from pages.login_page import LoginPage
from tests.driver_setup import driver_setup
import pytest

def test_login(driver_setup):
    driver = driver_setup
    driver.get("file:///D:/OS/Desktop/Learning_Software_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/login.html")
    # Login
    login = LoginPage(driver)
    login.login("testuser", "password")
    assert "Welcome" in driver.page_source or driver.title
    print("Login successful")
    
