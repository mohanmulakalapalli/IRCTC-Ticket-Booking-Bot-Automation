from selenium.webdriver.common.by import By

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.bookingSummary = (By.ID, "bookingSummary")
        self.pnrDetails = (By.ID, "pnrDetails")
        

    def payment(self, bookingSummary, pnrDetails):
        booking = self.driver.find_element(*self.bookingSummary)
        pnr = self.driver.find_element(*self.pnrDetails)
        return booking, pnr
        