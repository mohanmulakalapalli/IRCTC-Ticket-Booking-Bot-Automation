from selenium import webdriver
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.booking_page import BookingPage
from pages.payment_page import PaymentPage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the mock login page
    driver.get("D:/OS/Desktop/Learning_Software_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/login.html")  

    # Step 2: Perform login
    login_page = LoginPage(driver)
    login_page.login("testuser", "testpass")
    time.sleep(2)

    # Step 3: Navigate to the search page and search for trains
    search_page = SearchPage(driver)
    search_page.search_trains("Delhi", "Mumbai", "2025-05-01")
    time.sleep(2)

    # Step 4: Select a train and proceed to booking
    booking_page = BookingPage(driver)
    # Enter passenger details one by one
    passengers = [
        {"name": "rajat Doe", "age": "32", "gender":"Male", "train_number": "12345","ticket_type":"Tatkal"}
    ]

    for passenger in passengers:
        # Wait for the passenger name input field to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Passenger Name']"))
        )
        booking_page.enter_passenger_details(
            passenger["name"], passenger["age"], passenger["gender"], passenger["train_number"], passenger["ticket_type"]
        )
        time.sleep(1)  

    print("Ticket booking flow completed successfully!")
    
    # Create an instance of PaymentPage
    payment_page = PaymentPage(driver)
    # Get Booking and PNR elements
    booking, pnr = payment_page.payment(None, None)

    # Print the text of Booking and PNR
    print(booking.text)
    print(pnr.text)

finally:
    # Close the browser
    driver.quit()