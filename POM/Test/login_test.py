import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global driver
        ser = Service(executable_path="../../driver/chromedriver.exe")
        cls.driver = webdriver.Chrome(service= ser)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.ID, "welcome").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")





