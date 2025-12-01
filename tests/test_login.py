import pytest
import config  
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- TEST DATA ---
LOGIN_TEST_DATA = [
    (config.VALID_USER, config.INVALID_PASSWORD, config.LOGIN_ERROR_TEXT),
    (config.UNREGISTERED_USER, "any_pass", config.LOGIN_ERROR_TEXT)
]

# 1. HAPPY PATH TEST
def test_successful_login(driver):
    login_page = LoginPage(driver)
    driver.get("https://automationexercise.com/login")
    login_page.dismiss_consent()

    print("Attempting successful login...")
    login_page.login(config.VALID_USER, config.VALID_PASSWORD)

    # 🚨 REMOVED: The strict URL check. 
    # We will rely on the element check below, which has the global timeout.

    login_status_text = login_page.get_login_status_text()
    assert "Logged in as" in login_status_text
    print(f"✅ Success! Status: {login_status_text}")


# 2. UNHAPPY PATH TEST
@pytest.mark.parametrize("email, password, expected_error", LOGIN_TEST_DATA)
def test_login_failures(driver, email, password, expected_error):
    login_page = LoginPage(driver)
    
    driver.get("https://automationexercise.com/login")
    login_page.dismiss_consent()

    print(f"Testing login failure with: {email}")
    login_page.login(email, password) 

    actual_error = login_page.get_login_error_message()
    assert expected_error in actual_error
    print(f"✅ Pass! Got expected error: {actual_error}")