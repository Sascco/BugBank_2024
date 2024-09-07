import data
import locators
from locators import locators
from selenium.webdriver.support.wait import WebDriverWait


class BugbankPage:

    def __init__(self, driver):
        self.driver = driver

# Sign Up Page
    def click_sign_up_button(self):
        self.driver.find_element(*locators.register_button).click()

    def set_email(self, email_input_box):
        self.driver.find_element(*locators.client_email_input_box).click()
        self.driver.find_element(*locators.client_email_input_box).send_keys(data.client_email)

    def set_customers_name(self, customers_name):
        self.driver.find_element(*locators.customers_name).click()
        self.driver.find_element(*locators.customers_name).send_keys(data.customers_name)

    def set_customers_pass(self, customers_pass):
        self.driver.find_element(*locators.customers_password).click()
        self.driver.find_element(*locators.customers_password).send_keys(data.client_password)

    def set_confirmation_pass(self, password_confirmation):
        self.driver.find_element(locators.customers_password_confirmation).click()
        self.driver.find_element(locators.customers_password_confirmation).send_keys(data.client_password)

    def balance_on_account(self, adding_balance):
        self.driver.find_element(locators.adding_balance_toggle).click()

#Landing Page

    def