from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import code_phone
import data
import time
import locators
from methods import UrbanRoutesPage
class TestUrbanRoutes:
    driver = None

    @classmethod

    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)
        cls.driver.maximize_window()

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        from_address = data.from_address
        to_address = data.to_address
        routes_page.set_route(from_address, to_address)
        assert routes_page.get_from() == from_address
        assert routes_page.get_to() == to_address

# Prueba 2 seleccion opcion confort
    def test_confort_active(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page = locators.UrbanRoutesPage.confort_active


#Prueba 3 comprobar campo del numero de telefono
    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        button_phone = locators.UrbanRoutesPage.button_phone
        number_phone = locators.UrbanRoutesPage.number_field
        button_next = locators.UrbanRoutesPage.selection_button_next
        phone_code = code_phone.retrieve_phone_code
        button_to_accept = locators.UrbanRoutesPage.button_accept

#Prueba 4 Comprobar agregar tarjetas
    def test_credit_card_is_filled(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page = locators.UrbanRoutesPage.methods_pay
        routes_page = locators.UrbanRoutesPage.to_add_card
        routes_page = locators.UrbanRoutesPage.card_number_field
        routes_page = data.card_number
        routes_page = locators.UrbanRoutesPage.card_code_field
        routes_page = data.card_code
        routes_page = locators.UrbanRoutesPage.botton_to_add


#Prueba 5 Comprobar agregar mensaje
    def test_message_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page = locators.UrbanRoutesPage.message_for_driver_field
        routes_page = data.message_for_driver

#Prueba 6 comprobar si se agrega pedido de manta y pañuelos
    def test_selecction_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page = locators.UrbanRoutesPage.requisitos_del_pedido_button
        routes_page = locators.UrbanRoutesPage.selecction_blanket

#Prueba 7 comprobar si se agregaron los dos helados
    def test_add_two_ice(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page = locators.UrbanRoutesPage.selecction_ice
        routes_page = locators.UrbanRoutesPage.selecction_ice

#Prueba 8
    def test_start_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page = locators.UrbanRoutesPage.smart_button_main

    @classmethod
    def teardown_class(cls):
        # Cerrar el navegador
        cls.driver.quit()
