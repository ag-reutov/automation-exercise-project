from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPage(BasePage):
    # --- LOCATORS ---
    PRODUCTS_LINK = (By.CSS_SELECTOR, 'a[href="/products"]') 
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    SEARCH_RESULTS_HEADING = (By.XPATH, "//h2[text()='Searched Products']")
    
    PRODUCT_WRAPPER = (By.CSS_SELECTOR, '.product-image-wrapper')
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'a[data-product-id="2"]')
    
    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, 'button[data-dismiss="modal"]')
    CART_LINK_HEADER = (By.CSS_SELECTOR, 'a[href="/view_cart"]') 

    # --- ACTIONS ---

    def navigate_to_products_page(self):
        self.click(self.PRODUCTS_LINK)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )

    def search_for_product(self, product_name):
        self.set(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BTN)

    def add_product_to_cart(self):
        wrapper_element = self.find(self.PRODUCT_WRAPPER)
        ActionChains(self.driver).move_to_element(wrapper_element).perform()
        self.click_js(self.ADD_TO_CART_BTN)

    def handle_success_modal(self):
        """Clicks 'Continue Shopping' and waits for the modal to close."""
        self.click(self.CONTINUE_SHOPPING_BTN)
        

        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(self.CONTINUE_SHOPPING_BTN)
        )
        
    def navigate_to_cart(self):
        """Clicks the main Cart link in the header."""
        self.click(self.CART_LINK_HEADER)