import unittest
from datetime import datetime
from PageObjects import SearchPage
from selenium import webdriver


class SearchTest(unittest.TestCase):

    """A sample test class to show how page object works"""

    def setUp(self):
        # This specific set of options are needed for docker or local headless executions
        # If you want to see it running live, comment all options
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1420,1080')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://www.google.com")

    def test_happy_search(self):
        search_page = SearchPage.Search(self.driver)
        search_page.set_query()
        search_page.click_search()
        now = datetime.now()
        assert search_page.results_visible()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

