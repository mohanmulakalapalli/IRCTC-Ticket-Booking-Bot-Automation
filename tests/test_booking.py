from selenium import webdriver
from pages.booking_page import BookingPage
import pytest
from tests.driver_setup import driver_setup

def test_booking(driver_setup):
        driver = driver_setup
        driver.get("D:/OS/Desktop/Learming_Saftware_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/booking.html")
        booking = BookingPage(driver)
        booking.enter_passenger_details("Ravi", "28", "123654")
        print("Booking successful")
        assert "Booking" in driver.page_source or driver.title