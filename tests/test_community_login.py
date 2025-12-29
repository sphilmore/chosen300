from pages.base_registration_form import BaseForm
from pages.community_page import CommunityUser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TestConfig


def test_community_service_registry(driver):
    page = CommunityUser(driver)
    form = BaseForm(driver)
    form.open()
    page.click_community_service_field()
    page.select_registration_type()
    form.wait_for_form()
    form.fill_registration_form(
        first=TestConfig.FIRST_NAME,
        last=TestConfig.LAST_NAME,
        email=TestConfig.EMAIL,
        phone=TestConfig.PHONE_COMMUNITY
    )
    page.reason_for_service()
    page.assigning_institution()
    form.continue_to_site_selection()
    
    # Assert navigation to site selection page - verify site selection element is present
    site_selection_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='west-philadelphia']"))
    )
    assert site_selection_button.is_displayed(), "Site selection page did not load - west-philadelphia button not found or not visible"


