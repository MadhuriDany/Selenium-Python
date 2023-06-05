import requests
from requests.auth import HTTPBasicAuth

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time
import urllib3
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from POM.UploadFile import UploadFile


user = 'admin'
password = "admin"
res = requests.get(UploadFile.url, auth=HTTPBasicAuth(user, password))
result = urllib3.connection_from_url(UploadFile.url)

    #################### Launching the Website ############################

class Unittest_UploadFile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(UploadFile.url)
        driver.maximize_window()


    #################### Test the Upload_File #########################

    def test_UploadFile(self):
        driver = self.driver
        time.sleep(1)
        driver.find_element(By.ID, UploadFile.id_1).send_keys("C://Users/GAMADHUR/Images/Image.jpg")
        time.sleep(1)
        driver.find_element(By.ID, UploadFile.id_2).click()
        time.sleep(1)

    def tearDown(self):
        driver = self.driver
        driver.close()
        driver.quit()



if __name__ == "__main__":
        unittest.main()


