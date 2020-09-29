from selenium.webdriver.common.by import By


class SearchLocators(object):
    """A class for main/search page locators."""
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')
    SEARCH_RESULTS = (By.CLASS_NAME, 'med')
