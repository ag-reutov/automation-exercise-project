from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find(self, locator):
      
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.find(locator).click()

    def click_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def set(self, locator, value):
        """Finds the element, clicks via JS to bypass ads, clears, and types."""
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)
        element.clear()
        element.send_keys(value)