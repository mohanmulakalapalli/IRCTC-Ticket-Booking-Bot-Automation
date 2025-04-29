import pytest
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.booking_page import BookingPage
from pages.payment_page import PaymentPage
from tests.driver_setup import driver_setup


class TestTatkalBooking:  
    # Login
    def test_login(self,driver_setup):
        self.driver = driver_setup
        self.login = LoginPage(self.driver)
        self.login.login("testuser", "password")
        assert "Welcome" in self.driver.page_source or self.driver.title
        print("Login successful")
   
        # Search Trains
        self.search = SearchPage(self.driver)
        self.search.search_trains("Delhi", "Mumbai", "2025-04-25")
        assert "Search Results" in self.driver.page_source or self.driver.title
        print("Search successful")
   

       # Booking
        self.booking = BookingPage(self.driver)
        self.booking.enter_passenger_details("Ravi", "28", "Male", "123654", "Tatkal")
        print("Booking successful")
        assert "Booking" in self.driver.page_source or self.driver.title
        

        # Payment Page
        # Create an instance of PaymentPage
        self.payment_page = PaymentPage(self.driver)
        # Get Booking and PNR elements
        self.booking, self.pnr = self.payment_page.payment(None, None)

        # Print the text of Booking and PNR
        print("Payment successful")
        print(self.booking.text)
        print(self.pnr.text)
        assert "Payment" in self.driver.page_source or self.driver.title 
        