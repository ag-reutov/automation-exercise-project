# Automation Exercise Project

A comprehensive Selenium-based test automation framework for testing e-commerce functionality, including user authentication, account management, and shopping workflows.

## 📋 Project Overview

This project automates test scenarios for an e-commerce platform using:
- **Selenium WebDriver** - Browser automation
- **Pytest** - Test framework
- **Python** - Programming language

### Test Coverage
- **User Authentication**: Login with valid/invalid credentials
- **User Registration**: Signup with account creation
- **Shopping**: Product browsing and cart management
- **Account Management**: User profile and address information

## 📁 Project Structure

```
automation-exercise-project/
├── config.py                    # Test credentials and configuration data
├── conftest.py                  # Pytest fixtures and setup/teardown
├── requirements.txt             # Python dependencies
├── setup_project.py             # Project initialization script
├── pages/                       # Page Object Model (POM)
│   ├── base_page.py            # Base class with common web element interactions
│   ├── login_page.py           # Login and signup page interactions
│   ├── products_page.py        # Product browsing functionality
│   └── account_info_page.py    # User account information management
└── tests/                       # Test cases
    ├── test_login.py           # Login and signup test scenarios
    ├── test_shopping.py        # Shopping and product test scenarios
    └── test_signup.py          # User registration test scenarios
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Chrome/Chromium browser
- ChromeDriver (compatible with your Chrome version)

### 1. Clone or Navigate to Project
```bash
cd automation-exercise-project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**PowerShell (Windows):**
```powershell
.\venv\Scripts\Activate
```

**Command Prompt (Windows):**
```cmd
venv\Scripts\activate.bat
```

**Git Bash / macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Test File
```bash
pytest tests/test_login.py
```

### Run Specific Test Case
```bash
pytest tests/test_login.py::test_login_with_valid_credentials
```

### Run with Verbose Output
```bash
pytest -v
```

### Run with Console Output (print statements)
```bash
pytest -s
```

### Run with Coverage Report
```bash
pytest --cov=tests
```

## 📋 Test Data & Configuration

### config.py
Contains all test data constants including:
- **Credentials**: Valid and invalid login credentials
- **Error Messages**: Expected error messages for validation
- **User Data**: Pre-defined user information for registration
- **Address Information**: Test address data
- **Search Terms**: Sample product search data

#### Key Variables:
```python
VALID_USER = "test_portfolio_cz@yopmail.com"
VALID_PASSWORD = "password123"
NEW_USER_EMAIL = f"test_user_{random_number}@yopmail.com"  # Dynamically generated
```

## 🏗️ Page Object Model (POM) Architecture

### BasePage (base_page.py)
The foundation class providing common element interaction methods:
- `find()` - Finds elements with wait for visibility
- `find_visible()` - Finds visible elements
- `click()` - Clicks elements
- `click_js()` - JavaScript click for stubborn elements
- `set()` - Sets text input values
- `take_screenshot()` - Captures screenshots

### Page Classes
Each page extends `BasePage` and implements:
- Page-specific element locators (CSS selectors, XPath)
- Business logic methods for user interactions

## 🔧 Test Execution Configuration

### conftest.py
Pytest configuration file with:
- **Chrome Driver Setup**:
  - Headless mode (no GUI)
  - Eager page load strategy (faster tests)
  - 1920x1080 window size
  - Image loading disabled (performance optimization)
  - 15-second page load timeout
  
- **Driver Fixture**: Function-scoped fixture that:
  - Creates a Chrome driver instance before each test
  - Closes the driver after each test (teardown)

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| selenium | 4.38.0 | Web browser automation |
| pytest | 9.0.1 | Test framework |
| trio | 0.32.0 | Async I/O support |
| certifi | 2025.11.12 | SSL certificates |

See `requirements.txt` for complete list.

## 💡 Best Practices Used

1. **Page Object Model**: Separates page logic from test logic
2. **Explicit Waits**: Uses WebDriverWait for reliable element detection
3. **Fixture-based Setup**: Pytest fixtures manage driver lifecycle
4. **Configuration Externalization**: Test data separated from test code
5. **Headless Execution**: Tests run faster without UI rendering
6. **Eager Page Loading**: Tests start faster with eager load strategy

## 🚀 CI/CD Considerations

- Tests configured to run in **headless mode** (no UI)
- No image loading for faster execution
- 30-second wait timeout for maximum stability
- Screenshot capability for debugging failures

## 📝 Writing New Tests

1. Create page methods in appropriate page class
2. Use locators from the page class
3. Leverage BasePage helper methods
4. Keep test assertions simple and focused
5. Use config.py for all test data

### Example Test Structure:
```python
def test_user_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    login_page.login("user@example.com", "password")
    assert login_page.is_user_logged_in()
```

## 🐛 Debugging

- Add `-s` flag to see print statements: `pytest -s`
- Use `driver.save_screenshot()` to capture state
- Check console output for element locator issues
- Disable headless mode for visual debugging (modify conftest.py)

## 📧 Contact & Support

For questions or issues, refer to the test output logs or check the specific test method implementation.

---

**Last Updated**: December 2025  
**Framework**: Selenium 4.38.0 + Pytest 9.0.1
