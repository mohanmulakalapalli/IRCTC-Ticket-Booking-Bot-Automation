import pytest
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.booking_page import BookingPage
from tests.driver_setup import driver_setup

# URL Constants
URL_Login = "D:/OS/Desktop/Learming_Saftware_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/login.html"
URL_Search = "D:/OS/Desktop/Learming_Saftware_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/search.html"
URL_Booking = "D:/OS/Desktop/Learming_Saftware_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/booking.html"
URL_Payment = "D:/OS/Desktop/Learming_Saftware_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/payment.html"

class TestTatkalBooking:
    
      
    # Login
    @pytest.mark.usefixtures("driver_setup")
    def test_login(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(URL_Login)
        self.login = LoginPage(self.driver)
        self.login.login("testuser", "password")
        assert "Welcome" in self.driver.page_source or self.driver.title
        print("Login successful")
   

    # Search Trains
    @pytest.mark.usefixtures("driver_setup")
    def test_search_trains(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(URL_Search)
        self.search = SearchPage(self.driver)
        self.search.search_trains("Delhi", "Mumbai", "2025-04-25")
        assert "Search Results" in self.driver.page_source or self.driver.title
        print("Search successful")
   

    # Booking
    @pytest.mark.usefixtures("driver_setup")
    def test_booking(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(URL_Booking)
        self.booking = BookingPage(self.driver)
        self.booking.enter_passenger_details("Ravi", "28", "123654")
        print("Booking successful")
        assert "Booking" in self.driver.page_source or self.driver.title
        

    # Assert Payment Page
    @pytest.mark.usefixtures("driver_setup")
    def test_payment_page(self, driver_setup):
        self.driver = driver_setup
        self.driver.get(URL_Payment)
        assert "Payment" in self.driver.page_source or self.driver.title 
        print("Payment successful")