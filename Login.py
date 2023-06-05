# #initiate chrome browser driver
# import time
# from selenium import webdriver
#
# import chromedriver_autoinstaller
# chromedriver_autoinstaller.install()
# driver = webdriver.Chrome()
# # driver = webdriver.Chrome("C:\SeleniumBrowserDrivers\chromedriver.exe")
#
# #maximize window
# driver.maximize_window()
# time.sleep(2)
#
# #navigate to zerobank or to another browser
# driver.get("http://the-internet.herokuapp.com/")
# time.sleep(2)
#
# #navigating back on browser
# # driver.back()
# # time.sleep(2)
#
# #navigate forward on browser
# # driver.forward()
# # time.sleep(2)
# #
# #refresh the page
# # driver.refresh()
# # time.sleep(2)
#
# #close browser
# driver.close()
#
# #quit browser
# driver.quit()


import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.common.by import By


class DragTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_drag_drop(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://jqueryui.com/draggable/')
        driver.switch_to.frame(0)
        source1 = driver.find_element(By.ID, 'draggable')
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(source1, 100, 100).perform()
        time.sleep(5)
        driver.get('https://jqueryui.com/droppable/')
        driver.switch_to.frame(0)
        source1 = driver.find_element(By.ID, 'draggable')
        target1 = driver.find_element(By.ID, 'droppable')
        actions2 = ActionChains(driver)
        actions2.drag_and_drop(source1, target1).perform()
        time.sleep(5)
        self.assertEqual("A", target1.text)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()








