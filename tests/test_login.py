import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import VALID_USER, VALID_PASSWORD
from pages.login_page import LoginPage

# Locator for the consent button
CONSENT_BTN = (By.CSS_SELECTOR, "button[aria-label='Consent']")


def test_successful_login(driver):
    # 1. Initialize the Page Object 
    login_page = LoginPage(driver)
    
    # 2. Go to the URL
    driver.get("https://automationexercise.com/login")
    
    # Dismiss consent dialog if it appears
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(CONSENT_BTN)).click()
        print("Consent dialog dismissed.")
    except Exception:
        pass
        
        
    # 3. Perform the Action (The Operator feeds the data)
    print("Attempting to login...")
    login_page.login(VALID_USER, VALID_PASSWORD)
    
    # 4. Verification (The Assertion)
    login_status_text = login_page.get_login_status_text()
    
    assert "Logged in as" in login_status_text
    print(f"✅ Success! Status: {login_status_text}")
    
    time.sleep(2)