from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # Signup Locators
    SIGNUP_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
    SIGNUP_EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP_BTN = (By.CSS_SELECTOR, '[data-qa="signup-button"]')

    # --- ACTIONS ---
    def login(self, email, password):
        self.set(self.EMAIL_FIELD, email)
        self.set(self.PASSWORD_FIELD, password)
        
        # 🚨 FINAL FIX: Use click_js() instead of click()
        # This bypasses the "Eager mode" race condition on headless servers.
        self.click_js(self.LOGIN_BTN)

    def get_login_status_text(self):
        return self.find(self.LOGGED_IN_AS_USER).text
    
    def get_login_error_message(self):
        return self.find(self.LOGIN_ERROR_MESSAGE).text

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