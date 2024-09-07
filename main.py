import data
import locators
from bug_bank import BugbankPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

#Start

class TestClass:
  def setUp(self):
    chrome_driver_path = r"C:\Users\Sascc\OneDrive\Desktop\chromedriver-win64\chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    self.driver = webdriver.Chrome(service=service)

  def test_setting_credentials(self):
    self.driver.get(data.bugBank_url)
    sleep(5)  # Let the page load for 5 seconds
    setting_credentials

  def tearDown(self):
    self.driver.quit()


test_instance = TestClass()
test_instance.setUp()
test_instance.test_setting_credentials()
test_instance.tearDown()