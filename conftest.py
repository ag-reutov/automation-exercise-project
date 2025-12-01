import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\n[Setup] Starting Chrome (Headless + Eager Mode)...")
    
    options = webdriver.ChromeOptions()
    
    # 1. HEADLESS MODE (Required for GitHub Actions/CI)
    options.add_argument("--headless=new") 
    
    # 2. PERFORMANCE & STABILITY
    options.page_load_strategy = 'eager' # Don't wait for full page load (ads)
    options.add_argument("--window-size=1920,1080") # Set size since we can't maximize
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox") # Required for Linux/CI environment
    options.add_argument("--disable-dev-shm-usage") # Required for Linux/CI environment
    
    driver = webdriver.Chrome(options=options)
    
    # Safety Net: If page takes > 10s to load, stop waiting
    driver.set_page_load_timeout(10)
    
    yield driver 
    
    print("\n[Teardown] Closing browser...")
    driver.quit()