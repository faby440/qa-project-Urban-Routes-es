from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import data
from selenium.common import WebDriverException

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

#ingresa direction desde
    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(data.address_from)

#ingresa direction hasta
    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

# click al boton  taxi
    def click_button_round(self):
        self.driver.find_element(*self.button_round).click()

# click seleccion taxi confort
    def click_confort_tcard_active(self):
        self.driver.find_element(*self.confort_tcard_active).click()

    def click_button_phone(self):
        self.driver.find_element(*self.button_phone).click()

# Ingresar numero de tlf
    def set_number(self, phone_number):
        self.driver.find_element(*self.number_field).send_keys(data.phone_number)

    def click_selection_button_next(self):
        self.driver.find_element(*self.selection_button_next).click()

    def click_code(self):
        self.driver.find_element(*self.code_field).click()

    def retrieve_phone_code(driver) -> str:
        """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
        Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
        El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""
    def get_number(self):
        return self.driver.find_element(self.number_field).get_property('value')

# click en metodo de pago
    def click_methods_pay(self):
        self.driver.find_element(*self.methods_pay).click()

# click agregar tarjeta
    def click_to_add_card(self):
        self.driver.find_element(*self.to_add_card).click()

#ingresa numero de tarjeta
    def set_card_number(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(data.card_number)
#ingresa numero de codigo
    def set_card_code(self, card_code):
        self.driver.find_element(*self.code_field).send_keys(data.card_code)

    def click_botton_to_add(self):
        self.driver.find_element(*self.botton_to_add).click()

    def click_close_button(self):
        self.driver.find_element(*self.close_button).click()

    def get_card_number(self):
        return self.driver.find_element(self.number_field).get_property('value')

    def get_card_code(self):
        return self.driver.find_element(*self.code_field).get_property('value')

#mensaje al conductor
    def set_message_for_driver(self, message_for_driver):
        self.driver.find_element(*self.message_for_driver_field).send_keys(data.message_for_driver)

#click para escoger manta y pañuelo
    def selecction_blanket(self):
       self.driver.find_element(*self.selecction_blanket).click()

 # pedir dos helados
    def selecction_ice(self):
        self.driver.find_element(*self.selecction_ice).click()

    def selecction_ice(self):
        self.driver.find_element(*self.selecction_ice).click()

#click aceptar taxi
    def smart_button_main(self):
        self.driver.find_element(*self.smart_button_main).click()