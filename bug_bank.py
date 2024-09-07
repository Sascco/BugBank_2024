import data
import locators
from locators import locators_list
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from locators import locators_list
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class BugbankPage:

    def __init__(self, driver):
        self.driver = driver

# Sign Up Page
    def click_sign_up_button(self):          # Metodo para hacer click en el botón "Registrarse" y crear una cuenta
        self.driver.find_element(*locators.register_button).click()

    def set_email(self, email_input_box):           # Metodo para ingresar el Correo electronico del usuario
        self.driver.find_element(*locators.client_email_input_box).click()
        self.driver.find_element(*locators.client_email_input_box).send_keys(data.client_email)

    def set_customers_name(self, customers_name):   # Metodo para ingresar el Nombre del usuario
        self.driver.find_element(*locators.customers_name).click()
        self.driver.find_element(*locators.customers_name).send_keys(data.customers_name)

    def set_customers_pass(self, customers_pass):           # Metodo para ingresar una contraseña
        self.driver.find_element(*locators.customers_password).click()
        self.driver.find_element(*locators.customers_password).send_keys(data.client_password)

    def set_confirmation_pass(self, password_confirmation):     # Metodo para ingresar la contraseña en el campo "Confirmar contraseña"
        self.driver.find_element(locators.customers_password_confirmation).click()
        self.driver.find_element(locators.customers_password_confirmation).send_keys(data.client_password)

    def balance_on_account(self, adding_balance):           # Metodo para hacer click en switch/toggle para crear la cuenta con saldo
        self.driver.find_element(locators.adding_balance_toggle).click()

#Landing Page

    def email_input(self, customers_email):     # Metodo para diligenciar email del usuario
        self.driver.find_element(*locators.client_email_input_box).send_keys(data.client_email)

    def pass_input(self, customers_pass):            # Metodo para diligenciar contraseña del usuario
        self.driver.find_element(*locators.client_password_input_box).send_keys(data.client_password)

    def login_button(self,click_login_button):      #Metodo para hacer click en botón acceder
        self.driver.find_element(*locators.login_button).click()

    # def


