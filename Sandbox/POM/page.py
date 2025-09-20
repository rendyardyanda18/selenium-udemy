from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException # for gpt 2

# tambahan gpt search()
from selenium.webdriver.common.keys import Keys
import time

from locators import MainPageLocators
from settings import WAIT_TIME

class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver

    def get_element(self,locator_type, locator_string):
        # return self.driver.find_element(locator_type, locator_string)   

       # (before gpt)
        # element = WebDriverWait(self.driver, WAIT_TIME).until(
        #     EC.presence_of_element_located((locator_type, locator_string))
        # )
        # return element 
        try:
            element = WebDriverWait(self.driver, WAIT_TIME).until(
                EC.visibility_of_element_located((locator_type, locator_string))
            )
            return element
        except NoSuchElementException as e:
            print(f"Element with {locator_type} of {locator_string} not found", e)
            raise


# (before gpt)
    # def get_text(self):
    #     element = self.get_element(locator_type, locator_string)
    #     return element.text

    # def enter_text(self, locator_type, locator_string, text):
    #     self.get_element(locator_type, locator_string).send_keys(text)

    # def click_button(self):
    #     self.get_element(locator_type, locator_string).click()

    # def get_page_title(self):
    #     return self.driver.title

#(gpt 1)
    # def enter_text(self, locator_type, locator_string, text):
    #     elem = self.get_element(locator_type, locator_string)
    #     elem.clear()   # opsional: bersihkan dulu
    #     elem.send_keys(text)

#(gpt 2)
    def enter_text(self, locator_type, locator_string, text):
        """Masukkan teks dengan retry dan pastikan value benar-benar masuk"""
        for attempt in range(3):
            try:
                elem = self.get_element(locator_type, locator_string)
                elem.clear()
                elem.send_keys(text)
                if elem.get_attribute("value") == text:
                    return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise

#(gpt 1)
    # def click_button(self, locator_type, locator_string):
    #     elem = WebDriverWait(self.driver, WAIT_TIME).until(
    #         EC.element_to_be_clickable((locator_type, locator_string))
    #     )
    #     elem.click()

#(gpt 2)
    def click_button(self, locator_type, locator_string):
        for attempt in range(3):  # coba ulang sampai 3 kali
            try:
                elem = WebDriverWait(self.driver, WAIT_TIME).until(
                    EC.element_to_be_clickable((locator_type, locator_string))
                )
                elem.click()
                return
            except StaleElementReferenceException:
                if attempt == 2:  # sudah 3x gagal
                    raise

    def get_page_title(self):
        return self.driver.title
    
class MainPage(BasePage):
#(before gpt)
    # def search(self, search_string):
    #     self.enter_text(*MainPageLocators.SEARCH_INPUT, search_string)
    #     self.click_button(*MainPageLocators.SEARCH_BUTTON)

    def search(self, search_string):
        elem = self.get_element(*MainPageLocators.SEARCH_INPUT)
        elem.clear()
        elem.send_keys(search_string)

        # ✅ pastikan value sudah masuk (Wikipedia kadang delay)
        for _ in range(3):
            if elem.get_attribute("value") == search_string:
                break
            time.sleep(0.5)
            elem.clear()
            elem.send_keys(search_string)

        # Klik tombol setelah input benar-benar ada
        self.click_button(*MainPageLocators.SEARCH_BUTTON)    


