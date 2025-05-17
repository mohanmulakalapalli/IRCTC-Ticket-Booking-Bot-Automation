from selenium import webdriver
from pages.search_page import SearchPage
from configurations.test_data import URL_Search
from utilities.customLogger import LogGen
import pytest
import os
from tests.conftest import driver


@pytest.mark.search
def test_search(driver):
    driver = driver
    # Logger
    logger = LogGen.loggen()
    logger.info("******* Starting test_Search**********")
    driver.get(URL_Search)
    driver.maximize_window()
    # Take screenshot of the search page
    screenshots_dir = "report/screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)  # Ensure the directory exists
    screenshot_path = os.path.join(screenshots_dir, "TS_search_page.png")  
    # Screenshot of the search page
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

    search = SearchPage(driver)
    search.search_trains("Delhi", "Mumbai", "2025-04-25")
    assert "Search Results" in driver.page_source or driver.title
    print("Search successful")
    # Check if the booking page is displayed
    booking_page = search.is_booking_page_displayed()
    if booking_page:
        # Take screenshot of the search results
        screenshot_path = os.path.join(screenshots_dir, "TS_search_results.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        logger.info("Booking page is displayed")  
        print("Booking page is displayed")
        assert True
    else:
        print("Booking page is not displayed")
        logger.error("Booking page is not displayed")
        # Take screenshot of the error
        screenshot_path = os.path.join(screenshots_dir, "TS_search_error.png")
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
        assert False

    # Close the driver
    driver.quit()
    # Log the end of the test
    logger.info("******* Ending test_Search **********")

    
      

   
    
