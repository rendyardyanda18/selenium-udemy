import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from page import MainPage
from settings import CHROMEDRIVER_PATH, WIKIPEDIA_URL


class WikipediaMainPAgeSearch(unittest.TestCase):

    def setUp(self):
        self.service = Service(executable_path=CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.set_window_size(1280, 800)  #tambahan gpt
        self.driver.get(WIKIPEDIA_URL)

    def test_search(self):
        search_text = 'Python (programming language)'
        main_page = MainPage(self.driver)
        main_page.search(search_text)
        self.assertEqual(
            search_text + ' - Wikipedia', main_page.get_page_title()
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()