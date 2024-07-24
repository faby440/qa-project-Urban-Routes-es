Nombre del proyecto: qa-project-Urban-Routes-es

Comprobando funcionalidades de la aplicacion Urban-Routes:
Pagina para solictar taxi que brinda diferentes tipos de autos para
la comodidad del cliente.

*Por medio de localizadores y metodos que imitan acciones de un usuario
como es: agregar texto, hacer click.

*Tambien aplicamos Clase By la cual nos ayuda a especificar
los criterios de la busqueda de los elementos.

(By.ID, "from"), (By.CLASS_NAME, '.button_round')

*Find_element nos ayuda a buscar elementos 

driver.find_element(*locators.UrbanRoutesPage.from_field)

*Usos de las esperas utilizamos las explicitas la cual detiene 
la prueba por un momento mientras carga.

ejemplo:
def wait_for_load_home_page(self):
    WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.from_field))


*Metodo send_keys() la utilizamos para llenar los campos de
entrada especifica.

Ejemplo:
self.driver.find_element(*locators.UrbanRoutesPage.from_field).send_keys(data.from_address)


*Para esta prueba usamos el metodo POM la cual facilita
el mantenimiento de los codigos de prueba.

*Metodo un paso fue utilizado en las pruebas que realiza varias 
acciones. Refleja cadena de eventos que lleva acabo.

ejemplo:
    def set_route(self, from_address, to_address):
        self.wait_for_load_home_page()
        self.set_from(data.from_address)
        self.set_to(data.to_address)



*Metodo Setup_class(): se llama una vez antes antes de todos los casos
de prueba. Econtrolador se crea desde el principio y todas las pruebas podran 
utilizarlo

ejemplo:
 def setup_class(cls):

*Se creo objeto de pagina que es UrbanRoutesPage

ejemplo:
class UrbanRoutesPage:

*Para declarar el metodo se coloco antes @classmethod que es un 
decorador que permite ampliar la funcionalidad de los metodos o funciones

*Usamos argumentos Cls y self no contiene ningun valor pero pasa
argumentos a la clase.

*para finalizar utilizamos Teardown_class()
el cual permite cerrar el navegador y detiene el driver si no lo 
especificamos el navegador permanecera abierto.


ejemplo:
 @classmethod
    def teardown_class(cls):
        # Cerrar el navegador
        cls.driver.quit()