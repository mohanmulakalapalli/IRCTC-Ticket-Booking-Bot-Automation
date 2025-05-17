from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.from_input = (By.XPATH, "//input[@placeholder='From Station']")
        self.to_input = (By.XPATH, "//input[@placeholder='To Station']")
        self.date_input = (By.XPATH, "//input[@type='date']")
        self.checkbox = (By.XPATH, "//label[2]/input[@type='checkbox']")
        self.search_button = (By.XPATH, "//button[text()='Search']")

    def search_trains(self, from_station, to_station, date):
        self.driver.find_element(*self.from_input).send_keys(from_station)
        self.driver.find_element(*self.to_input).send_keys(to_station)
        self.driver.find_element(*self.date_input).send_keys(date)
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.search_button).click()
    
    def is_booking_page_displayed(self):
        try:
            self.driver.find_element(By.XPATH, "//h2[text()='Booking Details']")
            return True
        except:
            return False
