import pytest
from selenium import webdriver
from pages.test_data import URL_Login
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver_setup():
    # Specify the path to chromedriver.exe
    service = Service(r"C:/Drivers/Chrome/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get(URL_Login)
    driver.maximize_window()
    yield driver
    driver.quit()