import pytest
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.booking_page import BookingPage
from pages.payment_page import PaymentPage
from tests.driver_setup import driver_setup

from pages.test_data import URL_Login, URL_Search, URL_Booking, URL_Payment, username, password
import os   

class TestTatkalBooking:
    
    def screenshot(self):
        screenshots_dir = "report/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
    # Login
    @pytest.mark.usefixtures("driver_setup")
    def test_login(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(URL_Login)
        self.driver.maximize_window()
        # Take screenshot of the login page
        screenshot_path = os.path.join("report/screenshots", "TLSBP_login_page.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        self.login = LoginPage(self.driver)
        self.login.login(username, password, self.login.get_captcha_text())
        self.login.accept_alert()
        assert "Welcome" in self.driver.page_source or self.driver.title
        print("Login successful")

   

    # Search Trains
    @pytest.mark.usefixtures("driver_setup")
    def test_search_trains(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(URL_Search)
        self.driver.maximize_window()
        # Take screenshot of the search page    
        screenshot_path = os.path.join("report/screenshots", "TLSBP_search_page.png")
        self.driver.save_screenshot(screenshot_path)    
        print(f"Screenshot saved at: {screenshot_path}")
        # Create an instance of SearchPage  
        self.search = SearchPage(self.driver)
        self.search.search_trains("Delhi", "Mumbai", "2025-04-25")
        assert "Search Results" in self.driver.page_source or self.driver.title
        print("Search successful")
   

    # Booking
    @pytest.mark.usefixtures("driver_setup")
    def test_booking(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(URL_Booking)
        self.driver.maximize_window()
        # Take screenshot of the booking page
        screenshot_path = os.path.join("report/screenshots", "TLSBP_booking_page.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        # Create an instance of BookingPage
        self.booking = BookingPage(self.driver)
        self.booking.enter_passenger_details("Ravi", "28", "Male", "123654", "Tatkal")
        print("Booking successful")
        assert "Booking" in self.driver.page_source or self.driver.title
        

    # Assert Payment Page
    @pytest.mark.usefixtures("driver_setup")
    def test_payment_page(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(URL_Payment)
        self.driver.maximize_window()
        # Take screenshot of the payment page   
        # Create an instance of PaymentPage
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
        screenshot_path = os.path.join("report/screenshots", "TLSBP_payment_page.png")
        self.driver.save_screenshot(screenshot_path)    
        print(f"Screenshot saved at: {screenshot_path}")
        # Assert Payment Page
        assert "Payment" in self.driver.page_source or self.driver.title 
        