import config
from pages.products_page import ProductsPage
from pages.login_page import LoginPage

def test_add_product_to_cart_flow(driver):
    products_page = ProductsPage(driver)
    login_page = LoginPage(driver) 

    # 1. Setup & Search
    driver.get("https://automationexercise.com/")
    login_page.dismiss_consent() 
    
    print("Navigating to Products page...")
    products_page.navigate_to_products_page()
    
    print(f"Searching for: {config.SEARCH_TERM}")
    products_page.search_for_product(config.SEARCH_TERM)
    
    # 2. Add to Cart
    print("Performing hover and Add to Cart action...")
    products_page.add_product_to_cart()

    # 3. Dismiss Modal 
    print("Handling success modal...")
    products_page.handle_success_modal()
    
    # 4. Final E2E Verification
    print("Navigating to Cart page for final verification...")
    products_page.navigate_to_cart()

    # Final Assertion: Verify we landed on the Cart page
    assert "view_cart" in driver.current_url
    
    
    print("✅ Success! Full E2E Shopping Journey completed.")