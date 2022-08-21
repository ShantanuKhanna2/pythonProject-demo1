# import pytest
#
# @pytest.fixture(scope="module")
# def setup():
#     print("Creating a DB connection")
#
#     yield
#     print("Closing a DB connection")
#
# @pytest.fixture(scope="function")
# def after():
#     print("Launching browser")
#
#     yield
#     print("Closing browser")
#
# @pytest.fixture(scope="function")
# def before():
#     print("Launching application")
#
#     yield
#     print("Closing application")
#
# @pytest.mark.usefixtures
# def test_to_log(setup, before):
#     print("Excuting login text")
#
# def test_to_login(setup, before):
#     print("Excuting login text")
#

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def get_data():

    return [

        ("way2automation.com","sadsaf"),
        ("java2automation.com","asssa")
    ]

def setup_function():
    global driver
    ser =Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=ser)
    driver.get("http://facebook.com")
    driver.maximize_window()

def teardown_function():
    driver.quit()

@pytest.mark.parametrize("username,password",get_data())
def test_login(username, password):
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID,"pass").send_keys(password)