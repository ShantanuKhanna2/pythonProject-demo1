from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.mark.functional
def test_setup():
    global driver
    ser = Service(executable_path="../driver/chromedriver.exe")
    driver = webdriver.Chrome(service= ser)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()

def test_login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()

# def test_teardown():
#     driver.close()
#     driver.quit()