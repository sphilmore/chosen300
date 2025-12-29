# Chosen 300 Volunteer App - Test Automation

A comprehensive Selenium WebDriver test automation framework for the Chosen 300 Volunteer Application using Python, pytest, and the Page Object Model (POM) design pattern.

## 🚀 Features

- **Page Object Model (POM)**: Clean, maintainable test architecture
- **Multi-browser Support**: Chrome, Edge, and Firefox
- **Automated Screenshots**: Captures screenshots automatically on test failures
- **HTML Reports**: Self-contained HTML reports with embedded screenshots
- **Comprehensive Test Coverage**: Positive and negative test scenarios
- **Robust Waits**: Explicit waits for reliable test execution

## 📁 Project Structure

```
chosen300/
├── pages/              # Page Object Model classes
│   ├── base_registration_form.py
│   ├── already_registered_page.py
│   ├── community_page.py
│   ├── donation_page.py
│   └── musician_register_login_page.py
├── tests/              # Test cases
│   ├── test_already_login.py
│   ├── test_community_login.py
│   ├── test_donations.py
│   ├── test_music_login.py
│   └── test_new_login.py
├── reports/            # Test reports and screenshots
│   ├── report.html
│   └── screenshots/
├── conftest.py         # Pytest configuration and fixtures
└── pytest.ini         # Pytest settings
```

## 🛠️ Setup

### Prerequisites

- Python 3.10 or higher
- Chrome/Edge/Firefox browser installed
- ChromeDriver/EdgeDriver/GeckoDriver (automatically managed by Selenium 4+)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd chosen300
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Copy the example file
cp .env.example .env
# Or on Windows:
copy .env.example .env
```

5. Edit `.env` file with your actual test credentials (see Environment Variables section below)

## 🔐 Environment Variables

This project uses environment variables to store sensitive test data like phone numbers.

### Setup

1. **Copy the example file**:
   ```bash
   cp .env.example .env
   ```
   Or manually create `.env` file from `.env.example`

2. **Edit `.env` file** with your actual test credentials:
   ```env
   TEST_PHONE_NUMBER=your_phone_number_here
   TEST_EMAIL=test@email.com
   TEST_FIRST_NAME=Test
   TEST_LAST_NAME=User
   ```

3. **Never commit `.env` file** - it's already in `.gitignore`

### Available Environment Variables

- `TEST_PHONE_NUMBER`: Phone number for login tests
- `TEST_PHONE_REGISTRATION`: Phone number for registration tests
- `TEST_PHONE_DONATION`: Phone number for donation tests
- `TEST_PHONE_MUSIC`: Phone number for music registration tests
- `TEST_PHONE_COMMUNITY`: Phone number for community service tests
- `TEST_EMAIL`: Email address for test accounts
- `TEST_FIRST_NAME`: First name for test accounts
- `TEST_LAST_NAME`: Last name for test accounts

## 🧪 Running Tests

### Run all tests:
```bash
pytest tests\ -v
```

### Run specific test file:
```bash
pytest tests\test_new_login.py -v
```

### Run specific test:
```bash
pytest tests\test_new_login.py::test_new_volunteer_registration -v
```

### Run with different browser:
```bash
pytest tests\ -v --browser=edge
pytest tests\ -v --browser=firefox
```

## 📊 Test Reports

After test execution, view the HTML report:
- **Location**: `reports/report.html`
- **Features**: 
  - Test results summary
  - Pass/fail status
  - Screenshots for failed tests
  - Execution details

Open the report in your browser to view detailed results.

## 📝 Test Scenarios

### New Volunteer Registration
- ✅ Complete registration flow
- ✅ Missing required fields validation

### Already Registered Users
- ✅ Login functionality
- ✅ Sign out functionality

### Community Service
- ✅ Community service registration

### Donations
- ✅ Donation registration flow

### Music Registration
- ✅ Music registration flow
- ✅ Missing primary instrument validation

## 🏗️ Architecture

### Page Object Model
The framework uses the POM pattern to separate page-specific logic from test logic:

- **BaseForm**: Base class with common registration functionality
- **Page Objects**: Specific page classes inheriting from BaseForm
- **Tests**: Clean test methods using page objects

### Key Components

- **conftest.py**: 
  - WebDriver fixture with multi-browser support
  - Automatic screenshot capture on failures
  - HTML report integration

- **BaseForm**: 
  - Common methods for all registration forms
  - Reusable wait utilities
  - Error message handling

## 🔧 Configuration

### Browser Selection
Default browser is Chrome. Change in `conftest.py` or via command line:
```bash
pytest --browser=edge
```

### Timeouts
Default timeout is 10 seconds. Modify `TIMEOUT` in `BaseForm` class.

## 📸 Screenshots

Screenshots are automatically captured when tests fail:
- **Location**: `reports/screenshots/`
- **Format**: `{test_name}_{timestamp}.png`
- **Integration**: Embedded in HTML reports

## 📄 License

This project is for portfolio/demonstration purposes.

## 👤 Author

Test Automation Framework - Portfolio Project

