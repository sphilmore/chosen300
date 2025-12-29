from pages.musician_register_login_page import MusicianRegistry
from config import TestConfig


def test_music_login(driver):
    page = MusicianRegistry(driver)
    page.open()
    page.click_musician_register_login_page()
    page.wait_for_form()
    page.fill_registration_form(
        first=TestConfig.FIRST_NAME,
        last=TestConfig.LAST_NAME,
        email=TestConfig.EMAIL,
        phone=TestConfig.PHONE_MUSIC
    )
    page.select_primary_instrument()
    page.waiver_acceptance()
    page.complete_music_registration()
    expected_message = "Please sign the waiver to continue"
    assert page.get_complete_music_registration_error_message() == expected_message


def test_missing_primary_instrument(driver):
    page = MusicianRegistry(driver)
    page.open()
    page.click_musician_register_login_page()
    page.wait_for_form()
    page.fill_registration_form(
        first=TestConfig.FIRST_NAME,
        last=TestConfig.LAST_NAME,
        email=TestConfig.EMAIL,
        phone=TestConfig.PHONE_MUSIC
    )
    page.complete_music_registration()
    expected_message = "Please select at least one instrument you play"
    assert page.get_primary_instrument_error_message() == expected_message
