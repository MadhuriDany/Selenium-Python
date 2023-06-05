import requests
from requests.auth import HTTPBasicAuth
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time
import urllib3
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from POM.JSAlerts import JSAlerts


user = 'admin'
password = "admin"
res = requests.get(JSAlerts.url, auth=HTTPBasicAuth(user, password))
result = urllib3.connection_from_url(JSAlerts.url)

    #################### Launching the Website ############################

class Unittest_JSAlerts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(JSAlerts.url)
        driver.maximize_window()
        time.sleep(3)

    #################### Test the JSAlerts #########################

    def test_JSAlerts(self):
        driver = self.driver
        driver.find_element(By.XPATH, JSAlerts.alert).click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(3)

        driver.find_element(By.XPATH, JSAlerts.confirm).click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(3)

        driver.find_element(By.XPATH, JSAlerts.confirm).click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(3)

        driver.find_element(By.XPATH, JSAlerts.prompt).click()
        time.sleep(2)
        driver.switch_to.alert.send_keys("Hello! Selenium-Python")
        driver.switch_to.alert.accept()
        time.sleep(3)

        driver.find_element(By.XPATH, JSAlerts.prompt).click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(3)


    def tearDown(self):
        driver = self.driver
        driver.close()
        # yield driver
        driver.quit()


if __name__ == "__main__":
    unittest.main()

