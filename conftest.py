import pytest
from selenium import webdriver

@pytest.fixture(scope="function")

def driver():

    print("\n[Setup] Starting Chrome...")
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    yield driver 
    
    print("\n[Teardown] Closing browser...")

    driver.quit()