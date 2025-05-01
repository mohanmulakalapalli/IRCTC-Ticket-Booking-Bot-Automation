from selenium.webdriver.common.by import By

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.bookingSummary = (By.ID, "bookingSummary")
        self.pnrDetails = (By.ID, "pnrDetails")
        self.name = (By.ID, "name")
        self.age = (By.ID, "age")
        self.gender = (By.ID, "gender")
        self.train = (By.ID, "train")
        self.ticketType = (By.ID, "type")
        self.pnr = (By.ID, "pnr")
        self.coach = (By.ID, "coach")
        self.berth = (By.ID, "berth")
        self.seat = (By.ID, "seat")

    def get_passenger_details(self):
        """Retrieve passenger details from the page."""
        passenger_details = {
            "name": self.driver.find_element(*self.name).text,
            "age": self.driver.find_element(*self.age).text,
            "gender": self.driver.find_element(*self.gender).text,
            "train": self.driver.find_element(*self.train).text,
            "ticket_type": self.driver.find_element(*self.ticketType).text,
        }
        return passenger_details

    def get_ticket_info(self):
        """Retrieve ticket information from the page."""
        ticket_info = {
            "pnr": self.driver.find_element(*self.pnr).text,
            "coach": self.driver.find_element(*self.coach).text,
            "berth": self.driver.find_element(*self.berth).text,
            "seat": self.driver.find_element(*self.seat).text,
        }
        return ticket_info

    # def payment(self):
    #     """Retrieve booking summary and PNR details."""
    #     booking = self.driver.find_element(*self.bookingSummary)
    #     pnr = self.driver.find_element(*self.pnrDetails)
    #     return booking, pnr