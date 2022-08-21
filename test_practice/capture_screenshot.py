from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service(executable_path="C:\\Users\Shantanuk\PycharmProjects\pythonProject-demo1\driver\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.implicitly_wait(10)

driver.get('https://www.way2automation.com/')
driver.save_screenshot("C:\\Users\Shantanuk\PycharmProjects\pythonProject-demo1\practice\screenshots\error.jpg")
driver.close()
driver.quit()