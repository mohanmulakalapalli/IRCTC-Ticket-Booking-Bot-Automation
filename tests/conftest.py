import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests with: chrome, firefox, edge")

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser").lower()
    if browser_name == "edge":
        service = EdgeService("C:/Drivers/Edge/msedgedriver.exe")
        driver = webdriver.Edge(service=service)
        print("Launching Edge browser.........")
    elif browser_name == "firefox":
        service = FirefoxService("C:/Drivers/Firefox/geckodriver.exe")
        driver = webdriver.Firefox(service=service)
        print("Launching Firefox browser.........")
    elif browser_name == "chrome":
        service = ChromeService("C:/Drivers/Chrome/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        print("Launching Chrome browser.........")
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()