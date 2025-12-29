from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_registration_form import BaseForm


class MusicianRegistry(BaseForm):
    """Page object for musician registration flow."""

    def __init__(self, driver):
        """Initialize the musician registry page object.
        
        Args:
            driver: Selenium WebDriver instance
        """
        super().__init__(driver)

    def click_musician_register_login_page(self):
        """Click the 'Register as Musician' button to start the musician registration process."""
        self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Register as Musician']"))
        ).click()

    def select_primary_instrument(self):
        """Select the primary instrument (Drums) from the dropdown."""
        element = self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))
        )
        element.click()

        option = self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//*[@role='option' and normalize-space()='Drums']"))
        )
        option.click()

    def complete_music_registration(self):
        """Click the 'Complete Registration' button to finalize the musician registration."""
        option = self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and normalize-space()='Complete Registration']"))
        )
        option.click()

    def get_complete_music_registration_error_message(self):
        """Get the error message displayed when waiver is not signed.

        Returns:
            str: The text content of the error message
        """
        message_error = self.wait().until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Please sign the waiver to continue']"))
        ).text
        return message_error

    def get_primary_instrument_error_message(self):
        """Get the error message displayed when no instrument is selected.

        Returns:
            str: The text content of the error message
        """
        error_message = self.wait().until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Please select at least one instrument you play']"))
        ).text
        return error_message
