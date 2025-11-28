import os

# Define the structure
folders = ["pages", "tests"]
files = [
    "pages/__init__.py",
    "pages/base_page.py",
    "pages/login_page.py",
    "tests/__init__.py",
    "tests/test_login.py",
    "conftest.py"
]

# Create Folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"✅ Created folder: {folder}")

# Create Files
for file in files:
    with open(file, 'w') as f:
        pass # Just creates an empty file
    print(f"✅ Created file: {file}")

print("\n🚀 Structure created successfully.")