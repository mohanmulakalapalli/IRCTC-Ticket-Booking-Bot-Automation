from selenium import webdriver
from pages.booking_page import BookingPage
from pages.payment_page import PaymentPage
from configurations.test_data import URL_Booking
from utilities.customLogger import LogGen
import os
import pytest
from tests.conftest import driver

def test_booking(driver):
        driver = driver
        # Logger
        logger = LogGen.loggen()
        logger.info("******* Starting test_Booking **********")
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

       
        # Check if the payment page is displayed
        if booking.is_payment_page_displayed():
                print("Payment page is displayed")
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
                logger.info("Payment page is displayed")
                print("Payment page is displayed")

                # Close the driver
                driver.quit()


                assert True
        else:
                print("Payment page is not displayed")
                logger.error("Payment page is not displayed")
                # Take screenshot of the error
                screenshot_path = os.path.join(screenshots_dir, "TB_booking_error.png")
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved at: {screenshot_path}")
                assert False
        # Close the driver
        driver.quit()
        # Log the end of the test
        logger.info("******* Ending test_Booking **********")