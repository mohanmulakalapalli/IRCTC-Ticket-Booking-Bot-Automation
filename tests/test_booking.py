from selenium import webdriver
from pages.booking_page import BookingPage
from pages.payment_page import PaymentPage
import pytest
from tests.driver_setup import driver_setup

def test_booking(driver_setup):
        driver = driver_setup
        driver.get("D:/OS/Desktop/Learning_Software_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/booking.html")
        booking = BookingPage(driver)
        booking.enter_passenger_details("Ravi", "28", "Male", "123654", "Tatkal")
        print("Booking successful")
        assert "Booking" in driver.page_source or driver.title

        # Create an instance of PaymentPage
        payment_page = PaymentPage(driver)
        # Get Booking and PNR elements
        booking, pnr = payment_page.payment(None, None)

        # Print the text of Booking and PNR
        print(booking.text)
        print(pnr.text)