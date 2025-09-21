import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from page import MainPage
from settings import CHROMEDRIVER_PATH, GOLDBUGS_URL


class GoldbugsMainPageFormFill(unittest.TestCase):
    """Class for testing form filling functionality
      on the Goldbugs main page."""

    def setUp(self) -> None:
        """Test-level setup method"""
        self.service = Service(executable_path=CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get(GOLDBUGS_URL)

    def test_invalid_form_submission(self):
        """Placeholder test method"""
        main_page = MainPage(self.driver)
        main_page.click_booking_form_link()
        main_page.fill_non_required_fields()
        main_page.submit_gold_bugs_form()
        self.assertIsNotNone(
            main_page.get_form_failure_div(),
            'Alert for required fields is missing'
            )

    def test_valid_form_submission(self):
        """Placeholder test method"""
        main_page = MainPage(self.driver)
        main_page.click_booking_form_link()
        main_page.fill_all_fields()
        main_page.submit_gold_bugs_form()
        self.assertIsNotNone(
            main_page.get_form_success_div(),
            'Form was not submitted successfully')

    def tearDown(self):
        """Test-level teardown method"""
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
