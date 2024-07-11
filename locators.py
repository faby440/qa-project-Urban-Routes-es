from selenium.webdriver.common.by import By
import data

class UrbanRoutesPage:

    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    taxi_button_round = (By.CLASS_NAME, "button_round")
    confort_tcard_active = (By.CLASS_NAME, "tcard_active")
    number_field = (By.ID, "number")
    selection_button_filled = (By.CLASS_NAME, "button_filled")
    to_add_title = (By.CLASS_NAME, "title")
    card_number_field = (By.ID, "number")
    card_code_field = (By.ID, "code")
    botton_full_field = (By.ID, "button_full")
    message_for_driver_field = (By.ID, "message_for_driver")
    blanket_slider_round = (By.CLASS_NAME, "slider_round")
    counter_plus = (By.CLASS_NAME, "counter_plus")
    smart_button_main = (By.CLASS_NAME, "smart_button_main")
