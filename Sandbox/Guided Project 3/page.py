from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
)
from settings import WAIT_TIME as WT

from locators import MainPageLocators


class BasePage(object):
    """Base class to initialize the base page
    that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator_string):
        """Get element from page"""
        # return self.find_element(locator_type, locator_string)
        # #before part 3
        try:
            element = WebDriverWait(self.driver, WT).until(
                EC.presence_of_element_located((locator_type, locator_string))
            )
            return element
        except NoSuchElementException as e:
            print(
                f'Element with {locator_type} of {locator_string} not found',
                e
                )

    def get_text(self, locator_type, locator_string):
        """Get text from element"""
        element = self.get_element(locator_type, locator_string)
        return element.text

    def enter_text(self, locator_type, locator_string, text):
        """Enter text into element"""
        self.get_element(locator_type, locator_string).send_keys(text)

    def click(self, locator_type, locator_string):
        """Click button on page"""
        # self.get_element(locator_type, locator_string).click()
        # #before part 3
        try:
            WebDriverWait(self.driver, WT).until(
                EC.element_to_be_clickable((locator_type, locator_string))
            ).click()
        except ElementClickInterceptedException as e:
            print(
                f'Element {locator_type} of {locator_string} not clickable',
                e
                )

    def select_by_value(self, locator_type, locator_string, value):
        """Select option in dropdown menu based on value"""
        select = Select(self.get_element(locator_type, locator_string))
        select.select_by_value(value)

    def submit_form(self, locator_type, locator_string):
        """Submit form element"""
        self.get_element(locator_type, locator_string).submit()


class MainPage(BasePage):
    """class for actions on the Gold Bugs home page"""

    def click_booking_form_link(self):
        """click booking form link to scroll"""
        # Before GPT
        # self.click(*MainPageLocators.BOOKING_FORM_ANCHOR)

        element = WebDriverWait(self.driver, WT).until(
            EC.presence_of_element_located(
                MainPageLocators.BOOKING_FORM_ANCHOR
                )
        )
        # Scroll biar pasti kelihatan
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element)
        # Klik pakai JS biar tidak blocked overlay
        self.driver.execute_script("arguments[0].click();", element)

    def fill_required_fields(self):
        """fill out only required fields in the form"""
        self.enter_text(*MainPageLocators.FIRST_NAME, 'John')
        self.enter_text(*MainPageLocators.LAST_NAME, 'Doe')
        self.enter_text(*MainPageLocators.EMAIL, 'johndoe@yopmail.com')
        self.enter_text(*MainPageLocators.SUBJECT, 'Love Your Band! vv')

    def fill_non_required_fields(self):
        """fill out only non-required fields in the form"""
        self.enter_text(
            *MainPageLocators.MESSAGE,
            'You are the greatest, I love your band!'
            )
        self.click(*MainPageLocators.NO_RESPONSE_REQUIRED_CHECKBOX)
        self.click(*MainPageLocators.PUBLIC_SHOW_RADIO_BUTTON)
        self.select_by_value(*MainPageLocators.SELECT_DROPDOWN, 'Other')
        self.click(*MainPageLocators.SURVEY_RADIO_BUTTON)

    def fill_all_fields(self):
        """fill out both required and non-required fields in the form"""
        self.fill_required_fields()
        self.fill_non_required_fields()

    def submit_gold_bugs_form(self):
        """submit the booking form"""
        self.submit_form(*MainPageLocators.FORM_ELEMENT)

    def get_form_failure_div(self):
        """get the div with the error message on failed fomr submission"""
        return self.get_element(*MainPageLocators.FORM_FAILURE_DIV)

    def get_form_success_div(self):
        """get the div with the 'thank you' message
        on successful form submission"""
        return self.get_element(*MainPageLocators.FORM_SUCCESS_DIV)
