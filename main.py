import data
import locators
from bug_bank import BugbankPage
from selenium import webdriver
from time import sleep


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()  # desired_capabilities = capabilities
        cls.driver.get(data.URBAN_ROUTES_URL)
        cls.driver.implicitly_wait(10)