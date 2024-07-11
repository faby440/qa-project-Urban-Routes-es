from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import json
import time
import data
from selenium.common import WebDriverException

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

#ingresa direction desde
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

#ingresa direction hasta
    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

# click al boton  taxi
    def click_button_round(self):
        self.driver.find_element(*self.button_round).click()

# click seleccion taxi confort
    def click_tcard_active(self):
        self.driver.find_element(*self.tcard_active).click()

# Ingresar numero de tlf
    def set_number(self, number_phone):
        self.driver.find_element(*self.number_field).send_keys(data.number_phone)

    def get_number(self):
        return self.driver.find_element(self.number_field).get_property('value')

# click en metodo de pago
    def click_button_filled(self):
        self.driver.find_element(*self.button_filled).click()

# click agregar tarjeta
    def click_title(self):
        self.driver.find_element(*self.locators.title).click()

# ingresa numero de tarjeta
    def set_card_number(self, card_number):
        self.driver.find_element(*self.number_field).send_keys(data.card_number)

#ingresa numero de codigo
    def set_code(self, card_code):
        self.driver.find_element(*self.code_field).send_keys(data.card_code)

    def get_card_number(self):
        return self.driver.find_element(self.number_field).get_property('value')

    def get_code(self):
        return self.driver.find_element(*self.code_field).get_property('value')

#clik en el boton agregar
    def click_button_full(self):
        self.driver.find_element(*self.button_full).click()

# mensaje al conductor
    def set_message_for_driver(self, message_for_driver):
        self.driver.find_element(*self.message_for_driver_field).send_keys(data.message_for_driver)

# click para escoger manta y pañuelo
    def slider_round(self):
       self.driver.find_element(*self.locators.slider_round).click()

 # pedir dos helados
    def counter_plus(self):
        self.driver.find_element(*self.locator.counter_plus).click()

    def counter_plus(self):
        self.driver.find_element(*self.locators.counter_plus).click()

 # click aceptar taxi
    def smart_button_main(self):
        self.driver.find_element(*self.locators.smart_button_main).click()

    def set_routes(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)