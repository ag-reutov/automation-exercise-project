from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):
    # --- LOCATORS ---
    PRODUCTS_LINK = (By.CSS_SELECTOR, 'a[href="/products"]') 
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    
    # Locator to verify search results header
    SEARCH_RESULTS_HEADING = (By.XPATH, "//h2[text()='Searched Products']")
    
    # --- ACTIONS ---

    def navigate_to_products_page(self):
        """Clicks the Products link and waits for the search bar to be ready."""
        # Note: We must locate the link from the current page's DOM (header)
        self.click(self.PRODUCTS_LINK)
        
        # 🚨 FIX: Explicitly wait until the search input field is interactable.
        # This solves the ElementNotInteractableException on page transition.
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )

    def search_for_product(self, product_name):
        """Types the product name and clicks the search button."""
        self.set(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BTN)

    def is_search_successful(self):
        """Verifies the 'Searched Products' header is visible."""
        return self.find(self.SEARCH_RESULTS_HEADING).text