from selenium.webdriver.common.by import By

class BookingPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.XPATH, "//input[@placeholder='Passenger Name']")
        self.age_input = (By.XPATH, "//input[@placeholder='Age']")
        self.gender_select = (By.XPATH, "//select[1]/option[text()='Female']")
        self.train_number_input = (By.XPATH, "//input[@placeholder='Train Number']")
        self.train_select = (By.XPATH, "//select[2]/option[text()='Tatkal']")
        self.proceed_button = (By.XPATH, "//button[text()='Proceed to Pay']")

    def enter_passenger_details(self, name, age, train_number):
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.age_input).send_keys(age)
        self.driver.find_element(*self.gender_select).click()
        self.driver.find_element(*self.train_number_input).send_keys(train_number)
        self.driver.find_element(*self.train_select).click()
        self.driver.find_element(*self.proceed_button).click()
