from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """Class with locator tuples for elements on the Gold Bugs main page"""

    # Required fields

    # (Before GPT)
    # FIRST_NAME = (By.NAME, 'fname')
    # LAST_NAME = (By.NAME, 'lname')
    # EMAIL = (By.NAME, 'email')
    # SUBJECT = (By.ID, 'text-yui_3_17_2_1_1664570076619_2729-field')

    # (After GPT)
    FIRST_NAME = (By.ID, "name-yui_3_17_2_1_1664570076619_2727-fname-field")
    LAST_NAME = (By.ID, "name-yui_3_17_2_1_1664570076619_2727-lname-field")
    EMAIL = (By.ID, "email-yui_3_17_2_1_1664570076619_2728-field")
    SUBJECT = (By.ID, "text-yui_3_17_2_1_1664570076619_2729-field")

    # Non-required fields

    # (Before GPT)
    # MESSAGE = (By.TAG_NAME, 'textarea')
    # NO_RESPONSE_REQUIRED_CHECKBOX = (
    #     By.XPATH, '//input[@value="No Response Required"]')
    # RESPONSE_REQUIRED_CHECKBOX = (
    #     By.XPATH, '//input[@value="Response Required"]')
    # PUBLIC_SHOW_RADIO_BUTTON = (
    #     By.XPATH, '//input[@value="Public Show"]')
    # SELECT_DROPDOWN = (
    #     By.ID, 'select-e1f50715-c8a7-48eb-bc99-2c245676068c-field')
    # SURVEY_RADIO_BUTTON = (By.XPATH, '//input[@value="2"]')

    # (After GPT)
    MESSAGE = (By.CSS_SELECTOR, "textarea[id^='textarea-'][id$='-field']")
    NO_RESPONSE_REQUIRED_CHECKBOX = (
        By.XPATH, "//input[@type='checkbox' and @value='No Response Required']"
    )
    RESPONSE_REQUIRED_CHECKBOX = (
        By.XPATH, "//input[@type='checkbox' and @value='Response Required']"
    )
    PUBLIC_SHOW_RADIO_BUTTON = (
        By.XPATH, "//label[.//span[contains(text(),'Public Show')]]"
    )
    SELECT_DROPDOWN = (
        By.ID,
        "select-e1f50715-c8a7-48eb-bc99-2c245676068c-field"
    )
    SURVEY_RADIO_BUTTON = (
        By.XPATH,
        "//fieldset[@data-question]//label[contains(., 'Agree')]"
    )

    # Other Elements

    # (Before GPT)
    # FORM_ELEMENT = (By.TAG_NAME, 'form')
    # FORM_FAILEURE_DIV = (By.CSS_SELECTOR, 'div.form-field-error')
    # FORM_SUCCESS_DIV = (By.CSS_SELECTOR, 'div.form-submission-text')
    # BOOKING_FORM_ANCHOR = (
    #     By.XPATH, '/html/body/div/header/div/div[2]/div/nav/div[4]/a')

    # (After GPT)
    FORM_ELEMENT = (By.TAG_NAME, "form")
    FORM_FAILURE_DIV = (By.CSS_SELECTOR, "p.form-field-error")
    FORM_SUCCESS_DIV = (By.CSS_SELECTOR, "div.form-submission-text")
    BOOKING_FORM_ANCHOR = (By.CSS_SELECTOR, "a[href='/#new-page-section']")
