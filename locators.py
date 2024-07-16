from selenium.webdriver.common.by import By
import data

class UrbanRoutesPage:

    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    taxi_button_round = (By.CLASS_NAME, ".button_round")
    confort_tcard_active = (By.ID, "tariff-card-4")
    button_phone = (By.CLASS_NAME, "np_text")
    number_field = (By.ID, "phone")
    selection_button_next = (By.CSS_SELECTOR, ".div[class='section active'] button[type='submit']")
    code_field = (By.XPATH, "//div[@class='input-container error']//input[@id='code']")
    button_accept = (By.XPATH, "//button[normalize-space()='Confirmar']")
    methods_pay = (By.CLASS_NAME, "pp-button_filled")
    to_add_card = (By.CLASS_NAME, "pp-plus")
    card_number_field = (By.ID, "number")
    card_code_field = (By.ID, "code")
    botton_to_add = (By.XPATH, "//button[normalize-space()='Agregar']")
    close_button = (By.XPATH, "//div[@class='payment-picker open']//div[@class='section active']//button[@class='close-button section-close']")
    message_for_driver_field = (By.ID, "comment")
    selecction_blanket = (By.XPATH, "//div[@class='workflow']//div[1]//div[1]//div[2]//div[1]//span[1]")
    selecction_ice = (By.XPATH, "//div[@class='r-group']//div[1]//div[1]//div[2]//div[1]//div[1]")
    smart_button_main = (By.CLASS_NAME, "smart-button-secondary")