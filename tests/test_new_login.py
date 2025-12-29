from pages.base_registration_form import BaseForm
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TestConfig


def test_new_volunteer_registration(driver):
    page = BaseForm(driver)
    page.open()
    page.click_register_as_new_volunteer()
    page.wait_for_form()
    page.fill_registration_form(
        first=TestConfig.FIRST_NAME,
        last=TestConfig.LAST_NAME,
        email=TestConfig.EMAIL,
        phone=TestConfig.PHONE_REGISTRATION
    )
    page.continue_to_site_selection()
    page.click_site_selection_radio_button()
    page.click_continue_to_waiver()
    page.waiver_acceptance()
    page.complete_registration()


def test_missing_required_fields(driver):
    page = BaseForm(driver)
    page.open()
    page.click_register_as_new_volunteer()
    page.wait_for_form()
    page.fill_registration_form(
        first=TestConfig.FIRST_NAME,
        last=TestConfig.LAST_NAME,
        phone=TestConfig.PHONE_REGISTRATION
    )
    page.continue_to_site_selection()
    assert page.get_error("Email address is required") == "Email address is required"