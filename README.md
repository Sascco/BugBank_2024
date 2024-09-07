
# BugBank_2024

¡Hola! 👋Somo el equipo 6 del Hackaton
🌻: Nosotros:
Marisol, Alain, Claudia, Sergio y Karina.

🙂 Proyectos :
Fake API → https://fakeapi.platzi.com/
Bugbank → bugbank-ui
Restful Booker → restful-booker
Documentación: https://docs.google.com/spreadsheets/d/15zxI2Il4YhJfbdf9e8pos4FR9_6j362L/edit?usp=sharing&ouid=117701476691019254617&rtpof=true&sd=true

# API testing: Restful-booker


## Descripción




> El presente proyecto contiene un conjunto de pruebas funcionales realizadas sobre la API de Booker, una API para gestionar reservas. Dentro de las pruebas se incluyeron las funcionalidades más relevantes para el usuario final mediante el uso de diferentes endpoints que permitian la creación de nuevas reservas, actualización de reservas existentes y eliminación de reservas. Al igual se verificó que se cumplan los parámetros de seguridad tomando en cuenta las autorizaciones necesarias para las funcionalidades correspondientes.





## Documentación utilizada


- [Apidoc] - https://restful-booker.herokuapp.com/apidoc/index.html
- [Postman] - https://learning.postman.com/docs/introduction/overview/
- [Jira]: Seguimiento de errores


## Tecnologías y herramientas utilizadas 

El proyecto hizo uso de las siguientes herramienta para desarrollar, verificar y gestionar incidencias.

                             Tecnologías y herramientas 
    Postman: Pruebas y documentación de API's
    Apidoc: Documentación 
    Jira: Gestor de incidencias
    


## Pruebas realizadas
    
- Endpoints probados
  - [POST] https://restful-booker.herokuapp.com/booking (Crear una reserva)
  - [GET] https://restful-booker.herokuapp.com/booking/:id (Obtener una reserva)
  - [PUT] https://restful-booker.herokuapp.com/booking/:id (Modificar una reserva)
  - [DELETE] https://restful-booker.herokuapp.com/booking/1 (Eliminar una reserva)

- Tipos de pruebas
  - Pruebas funcionales: validación de las respuestas y lógica de los endpoints

 
## Resultados de las pruebas 

Las pruebas se desarrollaron en el siguiente archivo, el cual contiene los links correspondientes hacia el gestor de incidencias donde se desarrollaron los informes de errores.

https://docs.google.com/spreadsheets/d/15zxI2Il4YhJfbdf9e8pos4FR9_6j362L/edit?usp=sharing&ouid=117701476691019254617&rtpof=true&sd=true 

## Proyectos Fake Api :
El presente proyecto contiene un conjunto de pruebas funcionales realizadas sobre la API Fake API e-commerce, una API que se puede utilizar con cualquier tipo de proyecto que necesite productos, usuarios, categorías, autenticación y usuarios en formato JSON. Puedes utilizar esta API para crear prototipos de comercio electrónico y aprender a conectarse a una API con las mejores prácticas. Dentro de las pruebas se incluyeron las funcionalidades más relevantes para el registro del usuario, de productos y de la creacion de nuevas categorias, usando de diferentes endpoints que permitian la creación de las pruebas necesarias.

## Documentación utilizada :
[Apidoc] - https://restful-booker.herokuapp.com/apidoc/index.html
[Web] - https://learning.postman.com/docs/introduction/overview/

## Tecnologías y herramientas utilizadas
Postman: Pruebas y documentación de API's
Apidoc: Documentación
Jira: Seguimiento de errores

Pruebas realizadas
Endpoints probados
[POST] https://api.escuelajs.co/api/v1/users/ (crear usuario)
[POST] https://api.escuelajs.co/api/v1/users/is-available (validar correo electronico)
[POST] https://api.escuelajs.co/api/v1/products/ (crear un producto)
[POST] https://api.escuelajs.co/api/v1/categories/ (crear una categoria)
[GET] https://api.escuelajs.co/api/v1/categories/1/products (Obtenga todos los productos por categoría)

## POM
El Modelo de Objetos de Página (POM, por sus siglas en inglés) es un patrón de diseño utilizado en pruebas automatizadas de interfaces de usuario (UI). Este patrón ayuda a crear una estructura más mantenible y legible al separar la lógica de la UI del código de las pruebas.

## Descripción del Modelo de Objetos de Página (POM)

Separación de Concerns:
Página de Objetos: Cada página de la aplicación se modela como una clase independiente. Esta clase contiene todos los elementos de la página y las acciones que se pueden realizar en ellos. Clases de Prueba: Las pruebas se centran en la lógica de verificación y utilizan las clases de página para interactuar con la UI. 2. Mejora de la Mantenibilidad:

Cuando los elementos de la UI cambian, solo se necesita actualizar el código en la clase de la página correspondiente, no en todas las pruebas que interactúan con esos elementos. 3. Reutilización de Código:

Las acciones comunes se pueden reutilizar en múltiples pruebas, lo que reduce la duplicación de código y facilita la creación de pruebas complejas. 4. Mayor Legibilidad:

Las clases de prueba son más legibles ya que se centran en las acciones y verificaciones en lugar de en los detalles de la implementación de la UI.

Guía de Instalación Rápida
Requisitos Previos
Sistema Operativo: Windows, macOS, o Linux
Editor: PyCharm (Community o Professional)
Paso 1: Instalar Python 3
Descargar Python:

Visita python.org y descarga la última versión de Python 3 para tu sistema operativo.
Instalar Python:

Ejecuta el instalador y asegúrate de seleccionar la opción "Add Python to PATH" antes de continuar con la instalación.
Paso 2: Instalar PyCharm
Descargar PyCharm:

Visita jetbrains.com/pycharm/download y descarga la versión Community (gratuita) o Professional.
Instalar PyCharm:

Ejecuta el instalador y sigue las instrucciones en pantalla para completar la instalación.
Paso 3: Crear un Nuevo Proyecto en PyCharm
Abrir PyCharm:

Abre PyCharm y selecciona File > New Project.
Configurar el Proyecto:

Elige una ubicación para tu nuevo proyecto.
Selecciona la versión de Python 3 que instalaste anteriormente como el intérprete del proyecto.
Paso 4: Instalar Pip
Verificar pip:
Pip se instala automáticamente con Python 3. Puedes verificar la instalación abriendo el terminal en PyCharm (View > Tool Windows > Terminal) y ejecutando:
pip --version
Paso 5: Instalar Selenium, WebDriver Manager y Pytest
Abrir el Terminal en PyCharm:

Ve a View > Tool Windows > Terminal.
Instalar Selenium y WebDriver Manager:

Ejecuta los siguientes comandos en el terminal:
pip install selenium
pip install webdriver-manager
Instalar pytest:

Ejecuta el siguiente comando en el terminal:
pip install pytest
Paso 6: Configurar WebDriver
Añadir Código de Ejemplo:

Crea un archivo Python (por ejemplo, test_example.py) y añade el siguiente código para verificar que todo está configurado correctamente:

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_google_search(setup):
    driver = setup
    driver.get("https://www.google.com")
    assert "Google" in driver.title
Ejecutar la Prueba:

Ejecuta el script desde el terminal usando pytest:
pytest test_example.py
Resumen de Comandos
# Verificar la instalación de pip
pip --version

# Instalar Selenium y WebDriver Manager
pip install selenium
pip install webdriver-manager

# Instalar pytest
pip install pytest

# Ejecutar las pruebas con pytest
pytest test_example.py
Como iniciar las pruebas...
Una vez tengas instalado Python, Pytest y Pycharm, vas a poder editar el codigo y ejecutar las pruebas que consideres necesarias ejecutando el archivo main.py.

En el archivo UrbanRoutesPage.py vas a encontrar los metodos, que utilizan los localizadores que se encuentran en el archivo Locators.py. Las pruebas están en la clase TestUrbanRoutes en el archivo Main.py.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)