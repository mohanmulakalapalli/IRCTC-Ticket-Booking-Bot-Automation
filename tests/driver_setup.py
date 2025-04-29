import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver_setup():
    # Specify the path to chromedriver.exe
    service = Service(r"C:/Drivers/Chrome/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get("file:///D:/OS/Desktop/Learning_Software_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/login.html")
    yield driver
    driver.quit()