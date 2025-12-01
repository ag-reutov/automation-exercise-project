import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Login Locators
    EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="login-email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-qa="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '[data-qa="login-button"]')
    # Signup Locators
    SIGNUP_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
    SIGNUP_EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP_BTN = (By.CSS_SELECTOR, '[data-qa="signup-button"]')
    # Confirmation Locator (Happy Path)
    LOGGED_IN_AS_USER = (By.XPATH, "//a[contains(text(), 'Logged in as')]")
    
    # Error Locator (Unhappy Path)
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//p[text()='Your email or password is incorrect!']")
    
    # Consent Modal Locator
    CONSENT_BTN = (By.CSS_SELECTOR, "button[aria-label='Consent']")

    # --- ACTIONS ---
    def login(self, email, password):
        self.set(self.EMAIL_FIELD, email)
        self.set(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)
        time.sleep(1) 
        
        self.click(self.LOGIN_BTN)
    
    def signup(self, name, email):
        self.set(self.SIGNUP_NAME_FIELD, name)
        self.set(self.SIGNUP_EMAIL_FIELD, email)
        self.click_js(self.SIGNUP_BTN)

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