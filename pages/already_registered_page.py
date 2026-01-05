from selenium.webdriver.common.by import By

from pages.base_registration_form import BaseForm
from selenium.webdriver.support import expected_conditions as EC

class User(BaseForm):
    """Page object for already registered user login flow."""

    def __init__(self, driver):
        """Initialize the user login page object.
        
        Args:
            driver: Selenium WebDriver instance
        """
        super().__init__(driver)

    def click_already_registered(self):
        """Click the 'Already Registered' button to access the login form."""
        self.wait().until(
            EC.presence_of_element_located((By.XPATH, "//button[.//span[normalize-space()='Already Registered']]"))
        ).click()

    def login(self, text):
        """Login with phone number or email.

        Args:
            text (str): Phone number or email address to use for login
        """
        self.wait().until(
            EC.presence_of_element_located((By.ID, "loginInput"))
        ).send_keys(text)
        self.wait().until(
            EC.presence_of_element_located((By.XPATH, "//div[@tabindex='0']//button[@type='submit']"))
        ).click()

    def get_success_login_message(self):
        """Get the success message displayed after successful login.

        Returns:
            str: The text content of the success toast message
        """
        message = self.wait().until(
            EC.visibility_of_element_located(((By.XPATH, "//li[@data-sonner-toast and @data-type='success' and @data-visible='true']")
))
        )
        return message.text

    def sign_out(self):
        """Click the sign out button to log out the current user."""
        self.wait().until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/' and .//button]"))
        ).click()

    def user_musician_role(self):
        self.wait().until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.//text()[normalize-space()='Musician']]")
            )
        ).click()

    def get_user_musician_role_message(self):
        success = self.wait().until(
            EC.element_to_be_clickable(
                (By.XPATH, "//li[@data-sonner-toast and @data-type='success']")
            )
        ).text
        return success


    def user_community_service_role(self):
        self.wait().until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.//text()[normalize-space()='Community Service']]")
            )

        ).click()
    def get_user_community_service_role_message(self):
            success = self.wait().until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//li[@data-sonner-toast and @data-type='success']")
                )
            ).text
            return success

    def user_musician_role_sign_out(self):
        self.wait().until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Sign Out']")
            )
        ).click()

    def user_community_role_sign_out(self):
        self.wait().until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Sign Out']")
            )
        ).click()


