from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseForm:
    """Base page object class for registration forms with common functionality."""
    
    TIMEOUT = 20
    # URL
    URL = "https://chosen-300-volunteer-app-prototype-pbgi.vercel.app/"

    def __init__(self, driver):
        """Initialize the base form with a WebDriver instance.

        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver

    def wait(self):
        """Create and return a WebDriverWait instance with the configured timeout.

        Returns:
            WebDriverWait: Wait instance with TIMEOUT seconds
        """
        return WebDriverWait(self.driver, self.TIMEOUT)

    def open(self):
        """Navigate to the base URL."""
        self.driver.get(self.URL)

    def click_register_as_new_volunteer(self):
        """Click the 'Register as New Volunteer' button on the homepage."""
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Register as New Volunteer']]"))
        ).click()

    def wait_for_form(self):
        """Wait for the registration form to be present on the page.

        Waits for the firstName field to appear, indicating the form is loaded.
        """
        self.wait().until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )

    def fill_registration_form(self, first=None, last=None, email=None, phone=None):
        """Fill out the registration form with provided information.

        Args:
            first (str, optional): First name
            last (str, optional): Last name
            email (str, optional): Email address
            phone (str, optional): Phone number
        """
        if first:
            self.driver.find_element(By.ID, "firstName").send_keys(first)
        if last:
            self.driver.find_element(By.ID, "lastName").send_keys(last)
        if email:
            self.driver.find_element(By.ID, "email").send_keys(email)
        if phone:
            self.driver.find_element(By.ID, "phone").send_keys(phone)

    def continue_to_site_selection(self):
        """Click the 'Continue to Site Selection' button to proceed to site selection page."""
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue to Site Selection']"))
        ).click()

    def click_site_selection_radio_button(self):
        """Click the West Philadelphia site selection radio button."""
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='west-philadelphia']"))
        ).click()

    def click_continue_to_waiver(self):
        """Click the 'Continue to Waiver' button to proceed to the waiver page."""
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue to Waiver']"))
        ).click()

    def waiver_acceptance(self):
        """Click the waiver acceptance checkbox to accept the terms."""
        self.wait().until(
            EC.element_to_be_clickable((By.ID, "waiver-acceptance"))
        ).click()

    def complete_registration(self):
        """Click the 'Complete Registration' button to finalize the registration process."""
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Complete Registration']"))
        ).click()

    def get_error(self, text):
        """Get the text of an error message element matching the provided text.

        Args:
            text (str): The error message text to search for

        Returns:
            str: The text content of the error message element
        """
        element = self.wait().until(
            EC.visibility_of_element_located((By.XPATH, f"//p[normalize-space()='{text}']"))
        )
        return element.text

