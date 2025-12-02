from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    # --- LOCATORS ---
    EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="login-email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-qa="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '[data-qa="login-button"]')
    
    LOGGED_IN_AS_USER = (By.XPATH, "//a[contains(text(), 'Logged in as')]")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//p[text()='Your email or password is incorrect!']")
    CONSENT_BTN = (By.CSS_SELECTOR, "button[aria-label='Consent']")

    SIGNUP_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
    SIGNUP_EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP_BTN = (By.CSS_SELECTOR, '[data-qa="signup-button"]')

    # --- ACTIONS ---
    def login(self, email, password):
        self.set(self.EMAIL_FIELD, email)
        
        # 1. Type Password
        password_element = self.find_visible(self.PASSWORD_FIELD)
        password_element.clear()
        password_element.send_keys(password)
        
        # 🚨 FIX: Hit ENTER instead of clicking the button
        password_element.send_keys(Keys.ENTER)

    def get_login_status_text(self):
        # 🚨 FIX: Using the highly stable find_visible() method for status text
        return self.find_visible(self.LOGGED_IN_AS_USER).text
    
    def get_login_error_message(self):
        return self.find_visible(self.LOGIN_ERROR_MESSAGE).text

    def dismiss_consent(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.CONSENT_BTN)).click()
            print("Consent dialog dismissed.")
        except Exception:
            pass

    def signup(self, name, email):
        self.set(self.SIGNUP_NAME_FIELD, name)
        self.set(self.SIGNUP_EMAIL_FIELD, email)
        self.click_js(self.SIGNUP_BTN)