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
        WebDriverWait(self.driver, 45).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.from_field))
#ingresa direction desde
    def set_from(self, from_address):
        self.driver.find_element(*locators.UrbanRoutesPage.from_field).send_keys(data.from_address)
        return self.driver.find_element(*locators.UrbanRoutesPage.from_field).text
#ingresa direction hasta
    def set_to(self, to_address):
        self.driver.find_element(*locators.UrbanRoutesPage.to_field).send_keys(data.to_address)
        return self.driver.find_element(*locators.UrbanRoutesPage.to_field).text
    def get_from(self):
         return self.driver.find_element(*locators.UrbanRoutesPage.from_field).get_property("value")
    def get_to(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.to_field).get_property("value")
        # Metodo un paso Ingreso de direccion
    def set_route(self, from_address, to_address):
        self.wait_for_load_home_page()
        self.set_from(data.from_address)
        self.set_to(data.to_address)

# Click al boton  taxi
    def wait_for_load_taxi_button_round(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.taxi_button_round))
    def check_button_round_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.taxi_button_round).is_enabled()
    def click_button_round(self):
        self.driver.find_element(*locators.UrbanRoutesPage.taxi_button_round).click()

# click seleccion taxi confort
    def wait_for_load_confor_active(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.confort_active))
    def check_confort_active_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.confort_active).is_enabled()
    def click_in_confort_active(self):
        self.driver.find_element(*locators.UrbanRoutesPage.confort_active).click()

#click en el campo agregar telefono
    def wait_for_load_button_phone(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.button_phone))
    def check_button_phone_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.button_phone).is_enabled()
    def click_button_phone(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.button_phone).click()

#Ingresar numero de tlf
    def wait_for_number(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.number_field))
    def set_number_phone(self, phone_number):
        self.driver.find_element(*locators.UrbanRoutesPage.number_field).send_keys(data.phone_number)
        return self.driver.find_element(*locators.UrbanRoutesPage.number_field).text
    def get_number_phone(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.number_field).get_property("value")
    def wait_for_load_button_next(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.selection_button_next))
    def check_button_next_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.selection_button_next).is_enabled()
#Click boton siguiente
    def click_selection_button_next(self):
        self.driver.find_element(*locators.UrbanRoutesPage.selection_button_next).click()

#Ventana emergente
#Agregamos codigo y click confirmar para asignar numero de telefono
    def wait_for_code(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.code_field))
    def set_code(self):
        code = code_phone.retrieve_phone_code(self.driver)
        self.driver.find_element(*locators.UrbanRoutesPage.code_field).send_keys(code)
    def get_code(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.code_field).get_property("value")

#Click aceptar
    def wait_for_button_accept(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.button_accept))
    def check_button_accept_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.button_accept).is_enabled()
    def click_button_accept(self):
        self.driver.find_element(*locators.UrbanRoutesPage.button_accept).click()
    def set_into_code(self, retrieve_phone_code):
        self.wait_for_code()
        self.set_code(code_phone.retrieve_phone_code)

#click en metodo de pago
    def wait_for_load_methods_pay(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.methods_pay))
    def check_methods_pay_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.methods_pay).is_enabled()
    def click_methods_pay(self):
        self.driver.find_element(*locators.UrbanRoutesPage.methods_pay).click()

#Click agregar tarjeta +
    def wait_for_load_add_card(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.to_add_card))
    def check_add_card_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.to_add_card).is_enabled()
    def click_to_add_card(self):
        self.driver.find_element(*locators.UrbanRoutesPage.to_add_card).click()

#Ingresa numero de tarjeta
    def wait_for_card_number(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.card_number_field))
    def set_card_number(self, card_number):
        self.driver.find_element(*locators.UrbanRoutesPage.card_number_field).send_keys(data.card_number)
        return self.driver.find_element(*locators.UrbanRoutesPage.card_number_field).text
    def get_card_number(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.card_number_field).get_property("value")

#Ingresa numero de codigo
    def wait_for_card_code(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.card_code_field))
    def set_card_code(self, card_code):
        self.driver.find_element(*locators.UrbanRoutesPage.card_code_field).send_keys(data.card_code)
        return self.driver.find_element(*locators.UrbanRoutesPage.card_code_field).text
    def get_code_card(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.card_code_field).get_property("value")

#click boton guardar
    def wait_for_load_button_to_add(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.botton_to_add))
    def check_button_to_add_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.botton_to_add).is_enabled()
    def click_button_to_add(self):
        self.driver.find_element(*locators.UrbanRoutesPage.botton_to_add).click()

#click boton cerrar
    def wait_for_load_close_button(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.close_button))
    def check_close_button_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.close_button).is_enabled()
    def click_close_button(self):
        self.driver.find_element(*locators.UrbanRoutesPage.close_button).click()
# Metodo 1 paso agregar tarjeta de credito
    def set_enter_credit_card(self, card_number, into_code):
        self.click_methods_pay()
        self.click_to_add_card()
        self.set_card_number(card_number)
        self.set_into_code()
        self.click_button_to_add()
        self.click_close_button()

#mensaje al conductor
    def wait_for_message_for_driver(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.message_for_driver_field))
    def set_message_for_driver(self, message_for_driver):
        self.driver.find_element(*locators.UrbanRoutesPage.message_for_driver_field).send_keys(data.message_for_driver)
        return self.driver.find_element(*locators.UrbanRoutesPage.message_for_driver_field).text
    def get_mensaje_for_driver(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.message_for_driver_field).get_property("value")

#Requisitos del pedido
#click para escoger manta y pañuelos
    def wait_for_load_selecction_blanket(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.selecction_blanket))
    def check_selecction_blanket_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.selecction_blanket).is_enabled()
    def click_selecction_blanket(self):
        self.driver.find_element(*locators.UrbanRoutesPage.selecction_blanket).click()

#Pedir dos helados
    def wait_for_load_selecction_ice(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.selecction_ice))
    def check_selecction_ice_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.selecction_ice).is_enabled()
    def click_selecction_ice(self):
        self.driver.find_element(*locators.UrbanRoutesPage.selecction_ice).click()
    def check_selecction_ice_cream_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.selecction_ice).is_enabled()
    def click_selecction_ice_cream(self):
        self.driver.find_element(*locators.UrbanRoutesPage.selecction_ice).click()

#Aparece modal para pedir taxi
    def wait_for_load_smart_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locators.UrbanRoutesPage.smart_button_main))
    def check_smart_button_is_enabled(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.smart_button_main).is_enabled()
    def click_smart_button(self):
        self.driver.find_element(*locators.UrbanRoutesPage.smart_button_main).click