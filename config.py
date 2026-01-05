import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class TestConfig:
    """Configuration class for test data from environment variables."""

    # User credentials
    PHONE_NUMBER = os.getenv('TEST_PHONE_NUMBER', 'your_phone_number_here')
    USER_PHONE_NUMBER = os.getenv('TEST_USERS_PHONE_NUMBER', 'your_phone_number_here')
    EMAIL = os.getenv('TEST_EMAIL', 'test@email.com')
    FIRST_NAME = os.getenv('TEST_FIRST_NAME', 'Test')
    LAST_NAME = os.getenv('TEST_LAST_NAME', 'User')


    # Additional phone numbers for different test scenarios
    PHONE_REGISTRATION = os.getenv('TEST_PHONE_REGISTRATION', 'your_registration_phone_here')
    PHONE_DONATION = os.getenv('TEST_PHONE_DONATION', 'your_donation_phone_here')
    PHONE_MUSIC = os.getenv('TEST_PHONE_MUSIC', 'your_music_phone_here')
    PHONE_COMMUNITY = os.getenv('TEST_PHONE_COMMUNITY', 'your_community_phone_here')

    @classmethod
    def get_phone_number(cls, test_type='default'):
        """Get phone number based on test type.

        Args:
            test_type (str): Type of test (default, registration, donation, music, community)

        Returns:
            str: Phone number for the specified test type
        """
        phone_map = {
            'default': cls.PHONE_NUMBER,
            'registration': cls.PHONE_REGISTRATION,
            'donation': cls.PHONE_DONATION,
            'music': cls.PHONE_MUSIC,
            'community': cls.PHONE_COMMUNITY
        }
        return phone_map.get(test_type, cls.PHONE_NUMBER)