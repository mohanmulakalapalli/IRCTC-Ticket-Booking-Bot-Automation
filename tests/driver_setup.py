from selenium import webdriver
from pages.login_page import LoginPage
import pytest

@pytest.fixture(scope="function")
def driver_setup():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

