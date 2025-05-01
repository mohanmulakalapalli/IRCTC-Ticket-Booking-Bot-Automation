from selenium import webdriver
from pages.booking_page import BookingPage
from pages.payment_page import PaymentPage
from pages.test_data import URL_Booking
import os
import pytest
from tests.driver_setup import driver_setup

def test_booking(driver_setup):
        driver = driver_setup
        driver.get(URL_Booking)
        driver.maximize_window()
        # Take screenshot of the booking page
        screenshots_dir = "report/screenshots"
        os.makedirs(screenshots_dir, exist_ok=True)  # Ensure the directory exists
        screenshot_path = os.path.join(screenshots_dir, "TB_booking_page.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        # Create an instance of BookingPage
        booking = BookingPage(driver)
        booking.enter_passenger_details("Ravi", "28", "Male", "123654", "Tatkal")
        print("Booking successful")
        assert "Booking" in driver.page_source or driver.title

        # Take screenshot of the booking result
        screenshot_path = os.path.join(screenshots_dir, "TB_booking_result.png")                
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")        
        # Create an instance of PaymentPage
        payment_page = PaymentPage(driver)

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