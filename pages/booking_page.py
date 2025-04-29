from selenium.webdriver.common.by import By

class BookingPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "passengerName")  # Updated to match the ID in booking.html
        self.age_input = (By.ID, "age")  # Updated to match the ID in booking.html
        self.gender_select = (By.ID, "gender")  # Updated to match the ID in booking.html
        self.train_number_input = (By.ID, "trainNumber")  # Updated to match the ID in booking.html
        self.ticket_type_select = (By.ID, "ticketType")  # Updated to match the ID in booking.html
        self.proceed_button = (By.XPATH, "//button[text()='Proceed to Pay']")  # No change needed

    def enter_passenger_details(self, name, age, gender, train_number, ticket_type):
        # Enter passenger name
        self.driver.find_element(*self.name_input).send_keys(name)
        # Enter age
        self.driver.find_element(*self.age_input).send_keys(age)
        # Select gender
        gender_dropdown = self.driver.find_element(*self.gender_select)
        for option in gender_dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text == gender:
                option.click()
                break
        # Enter train number
        self.driver.find_element(*self.train_number_input).send_keys(train_number)
        # Select ticket type
        ticket_type_dropdown = self.driver.find_element(*self.ticket_type_select)
        for option in ticket_type_dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text == ticket_type:
                option.click()
                break
        # Click the proceed button
        self.driver.find_element(*self.proceed_button).click()