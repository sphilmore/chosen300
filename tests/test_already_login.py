from pages.already_registered_page import User
from config import TestConfig


def test_already_login_user(driver):
    page = User(driver)
    page.open()
    page.click_already_registered()
    page.login(TestConfig.PHONE_NUMBER)
    success_message = page.get_success_login_message()
    print(f"\nSuccess login message: '{success_message}'")
    assert success_message, "Success login message should not be empty"
    page.sign_out()


def test_user_musician_role(driver):
    page = User(driver)
    page.open()
    page.click_already_registered()
    page.login(TestConfig.USER_PHONE_NUMBER)
    page.user_musician_role()
    success_message = page.get_user_musician_role_message()
    print(f"\nMusician role success message: '{success_message}'")
    assert success_message, "Musician role success message should not be empty"
    page.user_musician_role_sign_out()


def test_user_community_role(driver):
    page = User(driver)
    page.open()
    page.click_already_registered()
    page.login(TestConfig.USER_PHONE_NUMBER)
    page.user_community_service_role()
    success_message = page.get_user_community_service_role_message()
    print(f"\nCommunity role success message: '{success_message}'")
    assert success_message, "Community role success message should not be empty"
    page.user_community_role_sign_out()

