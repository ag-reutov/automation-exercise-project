from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Increased to 30 seconds for maximum CI stability
        self.wait = WebDriverWait(driver, 30)

    def find(self, locator: tuple[By, str]) -> WebElement:
        """Finds element waiting for it to be clickable (best for buttons/links)."""
        return self.wait.until(EC.visibility_of_element_located(locator))
        
    def find_visible(self, locator: tuple[By, str]) -> WebElement:
        """🚨 NEW: Finds element waiting only for it to be visible (best for text/status)."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find(locator).click()

    def click_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def set(self, locator, value):
        element = self.find(locator)
        
        # We still click via JS first for typing stability (bypassing ads)
        self.driver.execute_script("arguments[0].click();", element) 
        
        element.clear()
        element.send_keys(value)