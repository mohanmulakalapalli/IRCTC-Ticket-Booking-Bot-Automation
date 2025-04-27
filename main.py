from selenium import webdriver
from pages.login_page import LoginPage
import time

driver = webdriver.Chrome()
driver.get("D:/OS/Desktop/Learming_Saftware_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/login.html")  

login_page = LoginPage(driver)
login_page.login("testuser", "testpass")
time.sleep(2)

# Continue other flows...
driver.quit()
