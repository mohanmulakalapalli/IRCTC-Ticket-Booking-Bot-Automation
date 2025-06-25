from selenium import webdriver
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.booking_page import BookingPage
from pages.payment_page import PaymentPage
from configurations.test_data import URL_Login, username, password
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class IRCTCTatkalBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.screenshots_dir = "report/screenshots/main"
        os.makedirs(self.screenshots_dir, exist_ok=True)  # Ensure the directory exists

    def take_screenshot(self, filename):
        screenshot_path = os.path.join(self.screenshots_dir, filename)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

    def open_login_page(self):
        self.driver.get(URL_Login)
        self.driver.maximize_window()
        time.sleep(2)  # Wait for the page to load
        self.take_screenshot("main_login.png")

    def perform_login(self):
        login_page = LoginPage(self.driver)
        captcha_text = login_page.get_captcha_text()
        login_page.login(username, password, captcha_text)
        login_page.accept_alert()
        time.sleep(2)

    def search_trains(self, source, destination, travel_date):
        self.take_screenshot("main_search.png")
        search_page = SearchPage(self.driver)
        search_page.search_trains(source, destination, travel_date)
        time.sleep(2)

    def book_tickets(self, passengers):
        self.take_screenshot("main_booking.png")
        booking_page = BookingPage(self.driver)

        for passenger in passengers:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Passenger Name']"))
            )
            booking_page.enter_passenger_details(
                passenger["name"], passenger["age"], passenger["gender"],
                passenger["train_number"], passenger["ticket_type"]
            )
            time.sleep(1)

        print("Ticket booking flow completed successfully!")

    def process_payment(self):
        payment_page = PaymentPage(self.driver)

        # Get passenger details
        passenger_details = payment_page.get_passenger_details()
        print("Passenger Details:")
        for key, value in passenger_details.items():
            print(f"{key.capitalize()}: {value}")

        # Get ticket information
        ticket_info = payment_page.get_ticket_info()
        print("\nTicket Information:")
        for key, value in ticket_info.items():
            print(f"{key.capitalize()}: {value}")

        self.take_screenshot("main_E_ticket.png")

    def run(self):
        try:
            self.open_login_page()
            self.perform_login()
            self.search_trains("Delhi", "Mumbai", "2025-07-01")
            passengers = [
                {"name": "John Doe", "age": "52", "gender": "Male", "train_number": "92345", "ticket_type": "Tatkal"}
            ]
            self.book_tickets(passengers)
            self.process_payment()
        finally:
            self.driver.quit()


if __name__ == "__main__":
    bot = IRCTCTatkalBot()
    bot.run()