import requests
from selenium import webdriver
import unittest
import Unittest_BrokenImages
import Unittest_UploadFile
import Unittest_Dropdown
import Unittest_JSAlerts
import urllib3
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
user = 'admin'
password = "admin"
# res = requests.get(JSAlerts.url, auth=HTTPBasicAuth(user, password))
# result = urllib3.connection_from_url(JSAlerts.url)

class Unittest_Suite(unittest.TestCase):

    def test_Assignment_Smoke_Suite(self):
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Unittest_BrokenImages.Unittest_BrokenImages),
            unittest.defaultTestLoader.loadTestsFromTestCase(Unittest_UploadFile.Unittest_UploadFile),
            unittest.defaultTestLoader.loadTestsFromTestCase(Unittest_Dropdown.Unittest_Dropdown),
            unittest.defaultTestLoader.loadTestsFromTestCase(Unittest_JSAlerts.Unittest_JSAlerts)
            ])

        runner = unittest.TextTestRunner()
        runner.run(self.suite)

if __name__ == "__main__":
    unittest.main()