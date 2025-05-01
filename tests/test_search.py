from selenium import webdriver
from pages.search_page import SearchPage
from pages.test_data import URL_Search
import pytest
import os
from tests.driver_setup import driver_setup

def test_search(driver_setup):
    driver = driver_setup
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
    # Take screenshot of the search results
    screenshot_path = os.path.join(screenshots_dir, "TS_search_results.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")    

   
    
