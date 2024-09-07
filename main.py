import data
import locators
from bug_bank import BugbankPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

# Start
class TestClass:
    def setUp(self):
        #chrome_driver_path = r"C:\Users\Sascc\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"
        chrome_driver_path = r"C:\Users\Sascc\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

    def test_setting_credentials(self):
        self.driver.get(data.bugBank_url)
        sleep(3)
        setting_credentials = BugbankPage(self.driver)
        sleep(2)
        setting_credentials.email_input(self.driver)
        sleep(2)
        setting_credentials.pass_input(self.driver)
        setting_credentials.login_button()
        sleep(3)
    def test_signup_account(self):
        self.driver.get(data.bugBank_url)
        signup_account = BugbankPage (self.driver)
        signup_account.click_sign_up_button(self.driver)
        signup_account.set_email(self.driver)
        signup_account.set_customers_name(self.driver)
        signup_account.set_customers_pass(self.driver)
        signup_account.set_confirmation_pass(self.driver)
        signup_account.adding_balance_new_account()


    def tearDown(self):
        self.driver.quit()

# Instantiate and run the tests
test_instance = TestClass()
test_instance.setUp()
test_instance.test_setting_credentials()
test_instance.tearDown()