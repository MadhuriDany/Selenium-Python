import requests
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time
import urllib3
import chromedriver_autoinstaller
from selenium.webdriver.support.select import Select

chromedriver_autoinstaller.install()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from POM.Dropdown import Dropdown


user = 'admin'
password = "admin"
res = requests.get(Dropdown.url, auth=HTTPBasicAuth(user, password))
result = urllib3.connection_from_url(Dropdown.url)

    #################### Launching the Website ############################

class Unittest_Dropdown(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(Dropdown.url)
        driver.maximize_window()


    #################### Test the Dropdown #########################

    def test_Dropdown(self):
        driver = self.driver
        dropdown = driver.find_element(By.ID, Dropdown.id)
        time.sleep(3)
        dd = Select(dropdown)
        dd.select_by_index(2)
        time.sleep(3)
        dd.select_by_value("2")
        time.sleep(3)
        dd.select_by_visible_text("Option 2")
        time.sleep(3)


    def tearDown(self):
        driver = self.driver
        driver.close()
        # yield driver
        driver.quit()


if __name__ == "__main__":
    unittest.main()

