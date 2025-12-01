from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class AccountInfoPage(BasePage):
    # --- LOCATORS ---
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-qa="password"]')
    DAY_DROPDOWN = (By.CSS_SELECTOR, '[data-qa="days"]')
    MONTH_DROPDOWN = (By.CSS_SELECTOR, '[data-qa="months"]')
    YEAR_DROPDOWN = (By.CSS_SELECTOR, '[data-qa="years"]')

    NEWSLETTER_CB = (By.ID, "newsletter")
    OFFERS_CB = (By.ID, "optin")

    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="first_name"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="last_name"]')
    COMPANY_FIELD = (By.CSS_SELECTOR, '[data-qa="company"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, '[data-qa="address"]')
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '[data-qa="country"]')
    STATE_FIELD = (By.CSS_SELECTOR, '[data-qa="state"]')
    CITY_FIELD = (By.CSS_SELECTOR, '[data-qa="city"]')
    ZIPCODE_FIELD = (By.CSS_SELECTOR, '[data-qa="zipcode"]')
    MOBILE_FIELD = (By.CSS_SELECTOR, '[data-qa="mobile_number"]')

    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, '[data-qa="create-account"]')
    
    # 🚨 NEW: Cleanup Locators
    CONTINUE_BTN = (By.CSS_SELECTOR, '[data-qa="continue-button"]')
    DELETE_ACC_LINK = (By.CSS_SELECTOR, 'a[href="/delete_account"]')

    # --- ACTIONS ---
    
    def fill_account_details(self, password, day, month, year):
        self.click(self.TITLE_MR)
        self.set(self.PASSWORD_FIELD, password)
        Select(self.find(self.DAY_DROPDOWN)).select_by_visible_text(str(day))
        Select(self.find(self.MONTH_DROPDOWN)).select_by_visible_text(str(month))
        Select(self.find(self.YEAR_DROPDOWN)).select_by_visible_text(str(year))
        self.click(self.NEWSLETTER_CB)
        self.click(self.OFFERS_CB)

    def fill_address_details(self, fname, lname, company, address, country, state, city, zipcode, mobile):
        self.set(self.FIRST_NAME_FIELD, fname)
        self.set(self.LAST_NAME_FIELD, lname)
        self.set(self.COMPANY_FIELD, company)
        self.set(self.ADDRESS_FIELD, address)
        Select(self.find(self.COUNTRY_DROPDOWN)).select_by_visible_text(country)
        self.set(self.STATE_FIELD, state)
        self.set(self.CITY_FIELD, city)
        self.set(self.ZIPCODE_FIELD, zipcode)
        self.set(self.MOBILE_FIELD, mobile)

    def click_create_account(self):
        self.click_js(self.CREATE_ACCOUNT_BTN)

    def delete_account(self):
        """
        1. Clicks 'Continue' to acknowledge account creation.
        2. Clicks 'Delete Account' in the navbar.
        3. Clicks 'Continue' again to confirm deletion.
        """
        # Step 1: Click Continue (Leaving 'Account Created' page)
        self.click(self.CONTINUE_BTN)
        
        # Step 2: Click Delete (In the Navbar)
        self.click(self.DELETE_ACC_LINK)
        
        # Step 3: Click Continue (Leaving 'Account Deleted' page)
        self.click(self.CONTINUE_BTN)