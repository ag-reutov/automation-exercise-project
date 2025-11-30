import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\n[Setup] Starting Chrome (Eager Mode)...")
    
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager' 
    

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=options)
    
    driver.set_page_load_timeout(10)

    yield driver 
    
    print("\n[Teardown] Closing browser...")
    driver.quit()