import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    print("\n[Setup] Starting Chrome (Headless + Eager + No Images)...")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") 
    options.page_load_strategy = 'eager' 
    options.add_argument("--window-size=1920,1080") 
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox") 
    options.add_argument("--disable-dev-shm-usage")
    
    # 🚨 SPEED FIX: Disable Images
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(15) # Keep this reasonable
    
    yield driver 
    
    print("\n[Teardown] Closing browser...")
    driver.quit()