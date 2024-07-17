from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import time
import locators


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

# Prueba 1 seleccion desde y hasta reaccionan correctamente al ingresarla
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(10)
        routes_page.wait_for_load_home_page()
        routes_page.set_route(data.from_address, data.to_address)
        assert routes_page.get_from() == data.from_address
        assert routes_page.get_to() == data.to_address

# Prueba 2 seleccion opcion confort
    def test_confort_tcard_active(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_confort_tcard_active()
        routes_page.click_confort_tcard_active()
        confort_tcard_active = routes_page.confort_tcard_active()
        assert confort_tcard_active == "True"

#Prueba 3 comprobar campo del numero de telefono
    def test_phone_number(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        button_phone = data.phone_number
        routes_page.set_number(data.phone_number)
        routes_page.click_button_accept()
        routes_page.get_code()
        routes_page.click_in_confirmar_button()
        telephone_description = routes_page.get_telephone_description()
        assert telephone_description == phone_number

#Prueba 4 Comprobar agregar tarjetas
    def test_credit_card_is_filled(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_credit_card()
        assert routes_page.get_number_credit_card() == data.card_number
        assert routes_page.get_code_credit_card() == data.card_code


#Prueba 5 Comprobar agregar mensaje
    def test_message_driver(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.message_for_driver()
        routes_page.wait_for_message_for_driver()
        routes_page.send_message_for_driver()
        text_message_for_driver = routes_page.get_message_for_driver()
        assert text_message_for_driver == data.message_for_driver

#Prueba 6 comprobar si se agrega pedido de manta y pañuelos
    def test_selecction_blanket(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.search_requisitos_del_pedido()
        routes_page.wait_for_pedido()
        routes_page.selecction_blanket()
        selecction_blanket = routes_page.selecction_blanket()
        assert selecction_blanket == "True"

#Prueba 7 comprobar si se agregaron los dos helados
    def add_two_ice(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.selecction_ice()
        routes_page.wait_for_icecream_button()
        routes_page.click_in_selecction_ice()
        is_icecream_selected = routes_page.ice_is_selected()
        assert is_ice_selected == "True"

