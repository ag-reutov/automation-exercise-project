from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class AccountInfoPage(BasePage):
    # --- LOCATORS (The Map) ---
    # Title
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    
    # Core Account Info
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-qa="password"]')
    DAY_DROPDOWN = (By.CSS_SELECTOR, '[data-qa="days"]')
    MONTH_DROPDOWN = (By.CSS_SELECTOR, '[data-qa="months"]')
    YEAR_DROPDOWN = (By.CSS_SELECTOR, '[data-qa="years"]')

    # Checkboxes
    NEWSLETTER_CB = (By.ID, "newsletter")
    OFFERS_CB = (By.ID, "optin")

    # Address Info
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="first_name"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '[data-qa="last_name"]')
    COMPANY_FIELD = (By.CSS_SELECTOR, '[data-qa="company"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, '[data-qa="address"]')
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '[data-qa="country"]')
    STATE_FIELD = (By.CSS_SELECTOR, '[data-qa="state"]')
    CITY_FIELD = (By.CSS_SELECTOR, '[data-qa="city"]')
    ZIPCODE_FIELD = (By.CSS_SELECTOR, '[data-qa="zipcode"]')
    MOBILE_FIELD = (By.CSS_SELECTOR, '[data-qa="mobile_number"]')

    # The Final Button
    CREATE_ACCOUNT_BTN = (By.CSS_SELECTOR, '[data-qa="create-account"]')

    # --- ACTIONS (The Logic) ---
    
    def fill_account_details(self, password, day, month, year):
        # 1. Title & Password
        self.click(self.TITLE_MR)
        self.set(self.PASSWORD_FIELD, password)
        
        # 2. Date of Birth (Using Select)
        Select(self.find(self.DAY_DROPDOWN)).select_by_visible_text(str(day))
        Select(self.find(self.MONTH_DROPDOWN)).select_by_visible_text(str(month))
        Select(self.find(self.YEAR_DROPDOWN)).select_by_visible_text(str(year))

        # 3. Checkboxes (Click them)
        self.click(self.NEWSLETTER_CB)
        self.click(self.OFFERS_CB)

    def fill_address_details(self, fname, lname, company, address, country, state, city, zipcode, mobile):
        self.set(self.FIRST_NAME_FIELD, fname)
        self.set(self.LAST_NAME_FIELD, lname)
        self.set(self.COMPANY_FIELD, company)
        self.set(self.ADDRESS_FIELD, address)
        
        # Country is a Dropdown!
        Select(self.find(self.COUNTRY_DROPDOWN)).select_by_visible_text(country)
        
        self.set(self.STATE_FIELD, state)
        self.set(self.CITY_FIELD, city)
        self.set(self.ZIPCODE_FIELD, zipcode)
        self.set(self.MOBILE_FIELD, mobile)

    def click_create_account(self):
        # Use JS Click to avoid being blocked by ads
        self.click_js(self.CREATE_ACCOUNT_BTN)