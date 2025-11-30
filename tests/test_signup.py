import config
from pages.login_page import LoginPage
from pages.account_info_page import AccountInfoPage

def test_signup_flow(driver):
    login_page = LoginPage(driver)
    account_page = AccountInfoPage(driver)
    
    # 1. Trigger Signup
    driver.get("https://automationexercise.com/login")
    login_page.dismiss_consent()
    
    print(f"Starting signup for: {config.NEW_USER_EMAIL}")
    login_page.signup(config.NEW_USER_NAME, config.NEW_USER_EMAIL)
    
    # 2. Fill Account Info
    print("Filling account details...")
    account_page.fill_account_details(
        password=config.VALID_PASSWORD, 
        day="12", month="May", year="1990"
    )
    
    # 3. Fill Address Info
    print("Filling address details...")
    account_page.fill_address_details(
        fname=config.FIRST_NAME,
        lname=config.LAST_NAME,
        company=config.COMPANY,
        address=config.ADDRESS,
        country=config.COUNTRY,
        state=config.STATE,
        city=config.CITY,
        zipcode=config.ZIPCODE,
        mobile=config.MOBILE
    )

    # 4. Create Account
    account_page.click_create_account()

    # 5. Verification (The End of the Identity Pillar!)
    # We check if the URL contains 'account_created'
    assert "account_created" in driver.current_url
    print("✅ Success! Account Successfully Created.")