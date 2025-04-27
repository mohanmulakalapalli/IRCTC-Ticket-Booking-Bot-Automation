from selenium import webdriver
from pages.search_page import SearchPage
import pytest
from tests.driver_setup import driver_setup

def test_search(driver_setup):
    driver = driver_setup
    driver.get("D:/OS/Desktop/Learming_Saftware_Related/Python_Automation_project/irctc_tatkal_bot/mock_site/search.html")
    search = SearchPage(driver)
    search.search_trains("Delhi", "Mumbai", "2025-04-25")
    assert "Search Results" in driver.page_source or driver.title
    print("Search successful")
   
    
