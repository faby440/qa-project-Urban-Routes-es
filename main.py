from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import code_phone
import data
import time
import locators
import methods
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

#Prueba 2 seleccion opcion confort
    def test_click_buttons(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_round()
        routes_page.click_in_confort_active()
        assert routes_page.check_button_round_is_enable
        assert routes_page.check_confort_active_is_enable()
#Prueba 3 comprobar campo del numero de telefono
    def test_set_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_button_phone()
        phone_number = data.phone_number
        routes_page.set_number_phone(phone_number)
        routes_page.click_selection_button_next()
        retrive_phone_code = code_phone.retrieve_phone_code
        routes_page.set_code()
        routes_page.click_button_accept()
        assert routes_page.check_button_phone_is_enable()
        assert routes_page.get_number_phone() == phone_number
        assert routes_page.check_button_next_is_enable
        assert routes_page.check_button_accept_is_enable
#Prueba 4 Comprobar agregar tarjetas
    def test_credit_add(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_methods_pay()
        routes_page.click_to_add_card()
        card_number = data.card_number
        routes_page.set_card_number(card_number)
        card_code = data.card_code
        routes_page.set_card_code(card_code)
        routes_page.click_button_to_add()
        routes_page.click_close_button()
        assert routes_page.check_methods_pay_is_enable()
        assert routes_page.check_add_card_is_enable()
        assert routes_page.get_card_number() == card_number
        assert routes_page.get_code_card() == card_code
        assert routes_page.check_add_card_is_enable()
        assert routes_page.check_close_button_is_enable()
#Prueba 5 Comprobar agregar mensaje
    def test_message_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(message_for_driver)
        assert  routes_page.get_mensaje_for_driver() == message_for_driver
#Prueba 6 comprobar si se agrega pedido de manta y pañuelos
    def test_selecction_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_selecction_blanket()
        assert routes_page.check_selecction_blanket_is_enable()

#Prueba 7 comprobar si se agregaron los dos helados
    def test_selecction_ice(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_selecction_ice()
        routes_page.click_selecction_ice_cream()
        assert routes_page.check_selecction_ice_is_enable()
        assert routes_page.check_selecction_ice_cream_is_enable()
#Prueba 8
    def test_start_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_smart_button()
        assert routes_page.check_smart_button_is_enabled()


    @classmethod
    def teardown_class(cls):
        # Cerrar el navegador
        cls.driver.quit()
