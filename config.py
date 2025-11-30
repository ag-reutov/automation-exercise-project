import random # <--- Import this to generate numbers

# --- CREDENTIALS (Happy Path) ---
VALID_USER = "test_portfolio_cz@yopmail.com"
VALID_PASSWORD = "password123"

# --- INVALID DATA (Unhappy Path) ---
INVALID_PASSWORD = "wrong_password123"
UNREGISTERED_USER = "definitely_not_registered_2025@yopmail.com"

# --- EXPECTED MESSAGES ---
LOGIN_ERROR_TEXT = "Your email or password is incorrect!"

# --- DYNAMIC DATA (For Signup) ---
random_number = random.randint(1000, 9999)
NEW_USER_EMAIL = f"test_user_{random_number}@yopmail.com"
NEW_USER_NAME = "Automated User"

# --- ADDRESS INFORMATION ---
FIRST_NAME = "Andrei"
LAST_NAME = "Student"
COMPANY = "Portfolio Corp"
ADDRESS = "123 Automation Street"
COUNTRY = "Canada" # Must match the dropdown text exactly
STATE = "Quebec"
CITY = "Montreal"
ZIPCODE = "H3Z 2Y7"
MOBILE = "1234567890"

# --- SEARCH DATA ---
SEARCH_TERM = "Tshirt"