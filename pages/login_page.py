from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # --- LOCATORS ---
    EMAIL_FIELD = (By.CSS_SELECTOR, '[data-qa="login-email"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-qa="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '[data-qa="login-button"]')
    LOGGED_IN_AS_USER = (By.XPATH, "//a[contains(text(), 'Logged in as')]")    
    # --- ACTIONS ---
    def login(self, email, password):
        self.set(self.EMAIL_FIELD, email)
        self.set(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BTN)

    def get_login_status_text(self):
        # This method uses BasePage.find() to wait for the confirmation element.
        return self.find(self.LOGGED_IN_AS_USER).text