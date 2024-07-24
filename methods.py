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


#Click al boton  taxi
    def check_button_round_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.taxi_button_round).is_enabled()
    def click_button_round(self):
        self.driver.find_element(*locators.UrbanRoutesPage.taxi_button_round).click()


#Metodo un paso Ingreso de direccion
    def set_route(self, from_address, to_address):
        self.wait_for_load_home_page()
        self.set_from(data.from_address)
        self.set_to(data.to_address)


# click seleccion taxi confort
    def wait_for_load_confor_active(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.confort_active))
    def check_confort_active_is_enable(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.confort_active).is_enabled()
    def click_in_confort_active(self):
        self.driver.find_element(*locators.UrbanRoutesPage.confort_active).click()


#click en el campo agregar telefono
    def click_button_phone(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.button_phone).click()


#Ingresar numero de tlf
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
        return self.driver.find_element(*locators.UrbanRoutesPage.code_field).send_keys(code_phone.retrieve_phone_code(driver))
    def click_button_accept(self):
        self.driver.find_element(*code_phone.retrieve_phone_code().selection_button_accept).click()

#click en metodo de pago
    def click_methods_pay(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.methods_pay).click()

#Click agregar tarjeta +
    def click_to_add_card(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.to_add_card).click()

#Ingresa numero de tarjeta
    def card_number(self):
        return self.driver.find_element(*locators.UrbanRoutesPage.card_number_field).send_keys(data.card_number)

#Ingresa numero de codigo
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
    def selecction_requisitos_del_pedido_is_selected(self):
        self.driver.find_element(*locators.UrbanRoutesPage.requisitos_del_pedido_button).is_selected()


#seleccionamos mantas y pañuelos
    def selecction_blanket(self):
        selecction_blanket = self.driver.find_element(*locators.UrbanRoutesPage.selecction_blanket)
        return self.driver.scroll_to_element(selecction_blanket)
    def wait_for_pedido(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.selecction_blanket))
    def selecction_blanket(self):
        self.driver.find_element(*locators.UrbanRoutesPage.selecction_blanket).click(*locators.UrbanRoutesPage.selecction_blanket)

#Verificamos seleccion de mantas y pañuelos
    def selecction_blanket_is_selected(self):
        self.driver.find_element(*locators.UrbanRoutesPage.selecction_blanket).is_selected()


#Pedir dos helados
    def selecction_ice(self):
        selecction_ice = self.driver.find_element(*locators.UrbanRoutesPage.selecction_ice)
        return self.driver.scroll_to_element(selecction_ice)
    def wait_for_selecction_ice(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.selecction_ice))
    def click_in_selecction_ice(self):
        self.driver.find_element(*locators.UrbanRoutesPage.selecction_ice).double_click(*locators.UrbanRoutesPage.selecction_ice)
#Verificamos que los helados fueron seleccionados
    def selecction_ice_is_selected(self):
        self.driver.find_element(*locators.UrbanRoutesPage.selecction_ice).is_selected()


#Aparece modal para pedir taxi
    def selecction_smart_button_main(self):
        smart_button_main = self.driver.find_element(*locators.UrbanRoutesPage.smart_button_main)
        return self.driver.scroll_to_element(smart_button_main)
    def wait_for_load_smart_button(self):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.smart_button_main))
    def click_smart_button(self):
        self.driver.find_element(*locators.UrbanRoutesPage.smart_button_main).click
    def selecction_smart_button_is_selected(self):
        self.driver.find_element(*locators.UrbanRoutesPage.smart_button_main).is_selected()
