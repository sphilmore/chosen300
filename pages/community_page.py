from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_registration_form import BaseForm


class CommunityUser(BaseForm):
    """Page object for Community Service registration flow."""
    
    def __init__(self, driver):
        super().__init__(driver)
        # Use wait() method from BaseForm instead of creating separate instance

    def click_community_service_field(self):
        """Click the 'Register for Community Service/Employment' button."""
        button = self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Register for Community Service/Employment']"))
        )
        button.click()

    def select_registration_type(self):
        """Select the community service registration type."""
        element = self.wait().until(
            EC.element_to_be_clickable((By.ID, "communityService"))
        )
        element.click()

    def reason_for_service(self):
        """Select the reason for service (Court ordered)."""
        element = self.wait().until(
            EC.element_to_be_clickable((By.ID, "serviceReason"))
        )
        element.click()

        option = self.wait().until(
            EC.element_to_be_clickable((By.XPATH, "//*[@role='option' and normalize-space()='Court ordered']"))
        )
        option.click()

    def assigning_institution(self):
        """Enter the assigning institution name."""
        element = self.wait().until(
            EC.presence_of_element_located((By.ID, "serviceInstitution"))
        )
        element.send_keys("Test")

