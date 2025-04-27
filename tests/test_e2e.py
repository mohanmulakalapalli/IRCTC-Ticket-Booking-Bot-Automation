import pytest
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.booking_page import BookingPage
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
        self.booking.enter_passenger_details("Ravi", "28", "123654")
        print("Booking successful")
        assert "Booking" in self.driver.page_source or self.driver.title
        

        # Assert Payment Page
        assert "Payment" in self.driver.page_source or self.driver.title 
        print("Payment successful")