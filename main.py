from selenium import webdriver
import data
from methods import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None
    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("perfLoggingPrefs", {'enableNetwork': True, 'enablePage': True})
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)
    def test_set_routes(self):
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(self, address_from)
        routes_page.set_to(self, address_to)
        # assert routes_page.get_from() == data.address_from
        #assert routes_page.get_to() == data.address_to

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()