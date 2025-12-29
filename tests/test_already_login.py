from pages.already_registered_page import User
from config import TestConfig


def test_already_login_user(driver):
    page = User(driver)
    page.open()
    page.click_already_registered()
    page.login(TestConfig.PHONE_NUMBER)
    expected = page.get_success_login_message()
    assert page.get_success_login_message() == expected
    page.sign_out()

