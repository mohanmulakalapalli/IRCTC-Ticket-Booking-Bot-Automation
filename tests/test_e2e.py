import os
import pytest
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.booking_page import BookingPage
from pages.payment_page import PaymentPage
from tests.conftest import driver
from configurations.test_data import URL_Login, username, password
from utilities.customLogger import LogGen


class TestTatkalBooking:
    """
    Test class for end-to-end testing of the Ticket booking process."""
    @pytest.fixture(autouse=True)
    def Logger(self):
        """Initialize the logger."""
        self.logger = LogGen.loggen()   
        self.logger.info("******* Starting test_E2E **********")
        yield
        self.logger.info("******* Ending test_E2E **********")

    def screenshot(self):
        screenshots_dir = "report/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)
    # Login
    @pytest.mark.e2e
    def test_login(self,driver):
        self.driver = driver
        self.driver.get(URL_Login)
        self.driver.maximize_window()
        screenshot_path = os.path.join("report/screenshots", "Te2e_login_page.png")
        self.driver.save_screenshot(screenshot_path)    
        print(f"Screenshot saved at: {screenshot_path}")
        self.login = LoginPage(self.driver)
        self.login.login(username, password, self.login.get_captcha_text())
        self.login.accept_alert()
        assert "Welcome" in self.driver.page_source or self.driver.title
        print("Login successful")
   
        # Search Trains
        screenshot_path = os.path.join("report/screenshots", "Te2e_search_page.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        self.search = SearchPage(self.driver)
        self.search.search_trains("Delhi", "Mumbai", "2025-04-25")
        assert "Search Results" in self.driver.page_source or self.driver.title
        print("Search successful")
   

       # Booking
        screenshot_path = os.path.join("report/screenshots", "Te2e_booking_page.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")

        self.booking = BookingPage(self.driver)
        self.booking.enter_passenger_details("Ravi", "28", "Male", "123654", "Tatkal")
        print("Booking successful")
        assert "Booking" in self.driver.page_source or self.driver.title
        

        # Payment Page
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
        screenshot_path = os.path.join("report/screenshots", "Te2e_payment_page.png")
        self.driver.save_screenshot(screenshot_path)    
        print(f"Screenshot saved at: {screenshot_path}")
        assert "Payment" in self.driver.page_source or self.driver.title

        self.driver.quit()
      
        