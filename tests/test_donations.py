from pages.donation_page import Donation
from config import TestConfig


def test_open_donation_page(driver):
    page = Donation(driver)
    page.open()
    page.click_donation_page()
    page.wait_for_form()
    page.donation_form_fill(
        first=TestConfig.FIRST_NAME,
        last=TestConfig.LAST_NAME,
        organization="ugh",
        email=TestConfig.EMAIL,
        phone=TestConfig.PHONE_DONATION
    )
    page.donation_continue_button()
    page.click_donation_category()
    page.enter_number_of_bags(10)
    page.donation_continue_button()