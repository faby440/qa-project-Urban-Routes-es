from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import time
import locators

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
#espera inicio de pagina
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.from_field))

#ingresa direction desde
    def set_from(self, from_address):
        self.driver.find_element(locators.from_field).send_keys(from_address)

#ingresa direction hasta
    def set_to(self, to_address):
        self.driver.find_element(locators.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(locators.to_field).get_property('value')

# click al boton  taxi
    def click_button_round(self):
        self.driver.find_element(locators.button_round).click()
#Metodo un paso Ingreso de direccion
    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.get_from()
        self.get_to()
        self.click_taxi_button()

    def wait_for_confort_tcard_active(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.confort_tcard_active))
# click seleccion taxi confort
    def click_confort_tcard_active(self):
        return self.driver.find_element(locators.confort_tcard_active).click()

    def confort_tcard_active(self):
        return self.driver.find_element(locators.confort_tcard_active).is_selected()

#click en el campo agregar telefono
    def click_button_phone(self):
        return self.driver.find_element(locators.button_phone).click()

# Ingresar numero de tlf
    def set_number(self, phone_number):
       return self.driver.find_element(locators.number_field).send_keys(phone_number)

    def click_selection_button_next(self):
        return self.driver.find_element(locators.selection_button_next).click()

    def get_telephone_description(self):
        return self.driver.find_element(locators.phone_number_field).text

#Ventana emergente
#agregamos codigo para agregar tlf y click confirmar

    def get_code(self):
        get_phone_code = retrieve_phone_code()
        return self.driver.find_element(locators.code_field).send_keys(get_phone_code)
    def click_button_accept(self):
        self.driver.find_element(locators.selection_button_accept).click()


# click en metodo de pago
    def click_methods_pay(self):
        return self.driver.find_element(locators.methods_pay).click()

# click agregar tarjeta +
    def click_to_add_card(self):
        return self.driver.find_element(locators.to_add_card).click()

#ingresa numero de tarjeta
    def card_number(self):
        return self.driver.find_element(locators.card_number_field).send_keys(data.card_number)
#ingresa numero de codigo
    def card_code(self):
        return self.driver.find_element(locators.card_code_field).send_keys(data.card_code)

#click boton guardar
    def click_botton_to_add(self):
        return self.driver.find_element(locators.botton_to_add).click()

    def get_number_credit_card(self):
        return self.driver.find_element(locators.add_card_field).text

    def get_code_credit_card(self):
        return self.driver.find_element(locators.code_field).text

    #click boton cerrar
    def click_close_button(self):
        return self.driver.find_element(locators.close_button).click()


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
        message_for_driver = self.driver.find_element(locators.message_for_driver)
        return self.driver.scroll_to_element(message_for_driver)
    def wait_for_message_for_driver(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.message_for_driver))

    def send_message_for_driver(self):
        self.driver.find_element(locators.message_for_driver).send_keys(data.message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(locators.message_for_driver).text



#Requisitos del pedido
#click para escoger manta y pañuelo
    def search_requisitos_del_pedido(self):
        requisitos_del_pedido = self.driver.find_element(locators.requisitos_del_pedido_button)
        return self.driver.scroll_to_element(requisitos_del_pedido)
    def wait_for_requisitos_del_pedido(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.requisitos_del_pedido_button))
    def click_requisitos_del_pedido(self):
        return self.driver.find_element(locators.requisitos_del_pedido_button).click()


#seleccionamos mantas y pañuelos
    def selecction_blanket(self):
        selecction_blanket = self.driver.find_element(locators.selecction_blanket)
        return self.driver.scroll_to_element(locators.selecction_blanket)
    def wait_for_pedido(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.selecction_blanket))
    def selecction_blanket(self):
        return self.driver.find_element(locators.selecction_blanket).click()

#verificamos seleccion de mantas y pañuelos
    def selecction_blanket(self):
        return self.driver.find_element(locators.selecction_blanket).is_selected()


 # pedir dos helados
    def selecction_ice(self):
        selecction_ice = self.driver.find_element(locators.selecction_ice)
        return self.driver.scroll_to_element(selecction_ice)

    def wait_for_selecction_ice(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.selecction_ice))

    def click_in_selecction_ice(self):
        self.driver.find_element(locators.selecction_ice).double_click(locators.helado_button)

    def selecction_ice_is_selected(self):
        self.driver.find_element(locators.selecction_ice).is_selected()
