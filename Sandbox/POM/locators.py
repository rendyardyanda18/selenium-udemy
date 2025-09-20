from selenium.webdriver.common.by import By

class MainPageLocators(object):
   
    SEARCH_INPUT = (By.ID, 'searchInput')
    # SEARCH_BUTTON = (By.ID, 'searchButton')
    # gunakan tombol Search, bukan tombol Go
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.cdx-search-input__end-button")