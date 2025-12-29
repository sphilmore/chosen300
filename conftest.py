import pytest
import os
from datetime import datetime
from selenium import webdriver
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser to use")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture test outcome for screenshot functionality."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Invalid Browser: {browser}")
    driver.maximize_window()
    yield driver
    
    # Capture screenshot on test failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        take_screenshot(driver, request.node)
    
    driver.quit()


def take_screenshot(driver, node):
    """Capture screenshot when a test fails."""
    # Create screenshots directory if it doesn't exist
    screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    
    # Generate screenshot filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    test_name = node.name.replace("::", "_").replace(" ", "_")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshots_dir, screenshot_name)
    
    try:
        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved: {screenshot_path}")
        
        # Attach screenshot to HTML report
        if hasattr(node, "rep_call"):
            if not hasattr(node.rep_call, "extra"):
                node.rep_call.extra = []
            
            rel_path = f"screenshots/{screenshot_name}"
            try:
                import pytest_html
                node.rep_call.extra.append(pytest_html.extras.image(rel_path))
            except ImportError:
                pass
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")