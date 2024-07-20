from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import code_phone
import data
import time
import locators

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.from_field))
#ingresa direction desde
    def get_from(self, from_adress):
        self.driver.find_element(*locators.UrbanRoutesPage.from_field).send_keys(data.from_address)
        return self.driver.find_element(*locators.UrbanRoutesPage.from_field).text
#ingresa direction hasta
    def get_to(self, to_address):
        self.driver.find_element(*locators.UrbanRoutesPage.to_field).send_keys(data.to_address)
        return self.driver.find_element(*locators.UrbanRoutesPage.to_field).text
# click al boton  taxi
    def click_button_round(self):
        self.driver.find_element(*locators.UrbanRoutesPage.taxi_button_round).click()
        check_sign_in_is_enabled(self)

#Metodo un paso Ingreso de direccion
    def set_route(self, from_address, to_address):
        self.wait_for_load_home_page()
        self.get_from(data.from_address)
        self.get_to(data.to_address)
        self.click_button_round()

# click seleccion taxi confort
    def check_confort_active_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.confort_active).is_enabled()
    def click_in_confort_active(self):
        self.driver.find_element(*locators.UrbanRoutesPage.confort_active).click()

#click en el campo agregar telefono
    def click_button_phone(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.button_phone).click()

# Ingresar numero de tlf
    def set_number(self, phone_number):
       return self.driver.find_element(*locators.UrbanRoutesPage.number_field).send_keys(data.phone_number)

    def click_selection_button_next(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.selection_button_next).click()

    def get_telephone_description(self):
        return self.driver.find_element(*code_phone.retrieve_phone_code()).text

#Ventana emergente
#agregamos codigo para agregar tlf y click confirmar
    def get_code(self):
        get_phone_code = retrieve_phone_code()
        return self.driver.find_element(*locators.UrbanRoutesPage.code_field).send_keys(code_phone.retrieve_phone_code())
    def click_button_accept(self):
        self.driver.find_element(*code_phone.retrieve_phone_code().selection_button_accept).click()

# click en metodo de pago
    def click_methods_pay(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.methods_pay).click()

# click agregar tarjeta +
    def click_to_add_card(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.to_add_card).click()

#ingresa numero de tarjeta
    def card_number(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.card_number_field).send_keys(data.card_number)
#ingresa numero de codigo
    def card_code(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.card_code_field).send_keys(data.card_code)

#click boton guardar
    def click_botton_to_add(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.botton_to_add).click()

    def get_number_credit_card(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.number_field).text

    def get_code_credit_card(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.code_field).text

    #click boton cerrar
    def click_close_button(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.close_button).click()


# Metodo 1 paso agregar tarjeta de credito
    def enter_credit_card(self):
        self.click_methods_pay()
        self.click_to_add_card()
        self.card_number()
        self.card_code()
        self.click_botton_to_add()
        self.click_close_button()

#mensaje al conductor
    def message_for_driver(self):
        message_for_driver = self.driver.find_element(*data.message_for_driver)
        return self.driver.scroll_to_element(message_for_driver)
    def wait_for_message_for_driver(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.message_for_driver_field))

    def send_message_for_driver(self):
        self.driver.find_element(*locators.UrbanRoutesPage.message_for_driver_field).send_keys(data.message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.message_for_driver_field).text


#Requisitos del pedido
#click para escoger manta y pañuelo
    def search_requisitos_del_pedido(self):
        requisitos_del_pedido = self.driver.find_element(*locators.UrbanRoutesPage.requisitos_del_pedido_button)
        return self.driver.scroll_to_element(requisitos_del_pedido)
    def wait_for_requisitos_del_pedido(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.requisitos_del_pedido_button))
    def click_requisitos_del_pedido(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.requisitos_del_pedido_button).click()


#seleccionamos mantas y pañuelos
    def selecction_blanket(self):
        selecction_blanket = self.driver.find_element(*locators.UrbanRoutesPage.selecction_blanket)
        return self.driver.scroll_to_element(*locators.UrbanRoutesPage.selecction_blanket)
    def wait_for_pedido(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.selecction_blanket))
    def selecction_blanket(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.selecction_blanket).click()

#verificamos seleccion de mantas y pañuelos
    def selecction_blanket(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.selecction_blanket).is_selected()

 # pedir dos helados
    def selecction_ice(self):
        selecction_ice = self.driver.find_element(*locators.UrbanRoutesPage.selecction_ice)
        return self.driver.scroll_to_element(selecction_ice)

    def wait_for_selecction_ice(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.selecction_ice))

    def click_in_selecction_ice(self):
        self.driver.find_element(locators.UrbanRoutesPage.selecction_ice).double_click(*locators.UrbanRoutesPage.selecction_ice)

    def selecction_ice_is_selected(self):
        self.driver.find_element(*locators.UrbanRoutesPage.selecction_ice).is_selected()

    def click_start_booton(self):
        self.driver.find_element(*locators.UrbanRoutesPage.smart_button_main).click

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
# no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)
        cls.driver.maximize_window()
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.from_address
        address_to = data.to_address
        routes_page.set_route(address_from, address_to)
        assert routes_page.set_from() == address_from
        assert routes_page.set_to() == address_to

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

    def test_start_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page = locators.UrbanRoutesPage.smart_button_main
