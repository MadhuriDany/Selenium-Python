import sys

import requests
from requests.auth import HTTPBasicAuth

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time
import urllib3
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from POM.BrokenImages import BrokenImages


user = 'admin'
password = "admin"
res = requests.get(BrokenImages.url, auth=HTTPBasicAuth(user, password))
result = urllib3.connection_from_url(BrokenImages.url)

    #################### Launching the Website ############################

class Unittest_BrokenImages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(BrokenImages.url)
        driver.maximize_window()

    #################### Test the Broken_Images #########################

    def test_BrokenImages(self):
        driver = self.driver
        time.sleep(1)
        iBrokenImageCount = 0

        image_list = driver.find_elements(By.TAG_NAME, "img")
        print('Total number of images on ' + BrokenImages.url + ' are ' + str(len(image_list)))

        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                if (response.status_code != 200):
                    print(img.get_attribute('outerHTML') + " is broken.")
                    iBrokenImageCount = (iBrokenImageCount + 1)

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")
        print('The page ' + BrokenImages.url + ' has ' + str(iBrokenImageCount) + ' broken images')

    def tearDown(self):
        driver = self.driver
        driver.close()
        driver.quit()



if __name__ == "__main__":
        unittest.main()


