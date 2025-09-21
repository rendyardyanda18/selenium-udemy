import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from page import MainPage
from settings import CHROMEDRIVER_PATH, GOLDBUGS_URL


class GoldbugsMainPageFormFill(unittest.TestCase):
    """Class for testing form filling functionality
      on the Goldbugs main page."""

    @classmethod
    def setUpClass(cls):
        """Class-level setup method"""
        cls.service = Service(executable_path=CHROMEDRIVER_PATH)
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.maximize_window()
        cls.driver.get(GOLDBUGS_URL)
        cls.main_page = MainPage(cls.driver)
        cls.main_page.click_booking_form_link()

    def setUp(self) -> None:
        """Test-level setup method"""
        pass

    def test_invalid_form_submission(self):
        """Test the rejection of a form with required fields not filled out"""
        self.main_page.fill_non_required_fields()
        self.main_page.submit_gold_bugs_form()
        self.assertIsNotNone(
            self.main_page.get_form_failure_div(),
            'Alert for required fields is missing'
            )

    def test_valid_form_submission(self):
        """Test the submission of a form with required fields filled out"""
        self.main_page.fill_required_fields()
        self.main_page.submit_gold_bugs_form()
        self.assertIsNotNone(
            self.main_page.get_form_success_div(),
            'Form was not submitted successfully')

    def tearDown(self):
        """Test-level teardown method"""
        pass

    @classmethod
    def tearDownClass(cls):
        """Class-level teardown method"""
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
