import config
from pages.products_page import ProductsPage
from pages.login_page import LoginPage

def test_product_search(driver):
    products_page = ProductsPage(driver)
    login_page = LoginPage(driver) 

    # 1. Start on Home Page
    driver.get("https://automationexercise.com/")
    
    login_page.dismiss_consent() # <--- 3. DISMISS AD

    # 2. Navigate to Products Page
    print("Navigating to Products page...")
    products_page.navigate_to_products_page()
    
    # 3. Perform Search
    print(f"Searching for: {config.SEARCH_TERM}")
    products_page.search_for_product(config.SEARCH_TERM)
    
    # 4. Verification
    # We assert that the "Searched Products" header is visible
    search_header = products_page.is_search_successful()
    assert "SEARCHED PRODUCTS" in search_header
    
    print(f"✅ Success! Search confirmed by header: {search_header}")