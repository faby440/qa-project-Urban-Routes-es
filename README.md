01-08-2024
  <em> # qa-project-Urban-Routes-es </em>
C:\Users\faby4\Documents\api_stand_tests\qa-project-Urban-Routes-es

## :hammer:Comprobando funcionalidades de la aplicacion Urban-Routes:
Es una pagina para solictar taxi que ofrece diferentes tipos de autos para
la comodidad del cliente.

- `Paso 1`:
Para el comienzo de nuestra prueba realizamos la instalacion de packages
pytes, assert, by, driver, pytest, self.

- `Paso 2`:
Luego definimos los localizadores con los cuales trabajaremos en la prueba 
los encontramos en: lotcators.py 

Para conseguirlos necesitamos la ayuda de DevTools son un conjunto de herramientas que ofrecen los navegadores 
para examinar la estructura y comportamiento de un sitio web.

los utilizados fueron:

By.ID, By.XPATH, By.CLASS_NAME, By.CSS_SELECTOR

- `Paso 3`:
En data.py definimos la informacion  que queremos agregar para 
la prueba de agregar texto.

- `Paso 4`:
1- Para trabajar con Selenium WebDriver, necesitamos conectarlo con nuestro IDE
2.-Para poder utilizar Selenium con Python, necesitamos instalar el paquete de Selenium.
3.-Importamos paquetes:

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

En esta prueba AUTOMATIZADA utilizamos el metodo POM 

- `Se crea una clase`: para el inicio de sesion la llamamos
   class UrbanRoutesPage:


- `Paso 5`:
Especificamos controlador a utilizar

utilizamos el método __init__
   self driver = driver

De esta manera, puedes configurar cualquier controlador que desees

-`DEFINIMOS LA INTERACCION DE LOS ELEMENTOS CON LOS SIGUIENTES METODOS`

- `Paso 6`:

Utilizamos esperas explícitas utilizando la clase WebDriverWait

def wait_for_load_home_page(self):
    WebDriverWait(self.driver, 45).until(expected_conditions.visibility_of_element_located(locators.UrbanRoutesPage.from_field))
Utilizamos estas dos condiciones 

#element_to_be_clickable: se puede hacer clic en el elemento.
#presence_of_element_located: el elemento está presente en la página.

- `Paso 8`:
Para rrellenar campo de entrada utilizamos el siguiente metodo 

def set_from(self, from_address):
    self.driver.find_element(*locators.UrbanRoutesPage.from_field).send_keys(data.from_address)
        return self.driver.find_element(*locators.UrbanRoutesPage.from_field).text

def get_from(self):
    return self.driver.find_element(*locators.UrbanRoutesPage.from_field).get_property("value")

- `Para probar que se puede hacer clic en el botón`:

def check_button_round_is_enable(self):
    return self.driver.find_element(*locators.UrbanRoutesPage.taxi_button_round).is_enabled()

- `Para hacer clic en el botón`:

def click_button_round(self):
    self.driver.find_element(*locators.UrbanRoutesPage.taxi_button_round).click()


- `Utilizamos el metodo un paso` es un método que contiene múltiples acciones o pruebas

def set_route(self, from_address, to_address):
    self.wait_for_load_home_page()
    self.set_from(data.from_address)
    self.set_to(data.to_address)

- `TEST`
- `Se crea una clase`: para los test
   class TestUrbanRoutes:


- `Para declarar el metodo`:se coloco antes @classmethod que es un 
decorador que permite ampliar la funcionalidad de los metodos o funciones


- `utilizar el método setup_class()`, puedes llamarlo una vez antes de todos los casos de prueba. 
El controlador se creará desde el principio y todas las pruebas podrán utilizarlo.

- `Creamos los controladores`:
from selenium.webdriver import DesiredCapabilities
capabilities = DesiredCapabilities.CHROME
capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
cls.driver = webdriver.Chrome()
cls.driver.get(data.urban_routes_url)
cls.driver.maximize_window()

*Usamos argumentos Cls y self no contiene ningun valor pero pasa
argumentos a la clase.

- `comenzamos las pruebas`
Cada prueba debe comenzar con test 

def test_set_route(self):
    routes_page = UrbanRoutesPage(self.driver)
    from_address = data.from_address
    to_address = data.to_address
    routes_page.set_route(from_address, to_address)
    assert routes_page.get_from() == from_address
    assert routes_page.get_to() == to_address

*para comprobar que se estan seleccionando los elementos utilizamos assert


*para finalizar utilizamos Teardown_class()
el cual permite cerrar el navegador y detiene el driver si no lo 
especificamos el navegador permanecera abierto.


ejemplo:
 @classmethod
    def teardown_class(cls):
        # Cerrar el navegador
        cls.driver.quit()

Al terminar nuestro proyecto lo compartimos por GIT 

Pasos a seguir:
nos ubicamos en nuestro Git Bash 
cd "C:\Users\faby4\Documents\api_stand_tests\qa-project-Urban-Routes-es" #REFERENCIA DE NUESTRO PROYECTO
*git status #VEMOS LOS CAMBIOS EN ROJO
*gitt add . #GUARDAMOS LOS CAMBIOS REALIZADOS
*git commit -m "proyecto1" 
 por ultimo git push -u origin master

de esta manera podemos guardar nuestro proyecto en nuestro repositorio GIT.