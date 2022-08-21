import time

import DDT_for_HCM

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service(executable_path="driver\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.implicitly_wait(10)

path = "C:\\Users\Shantanuk\PycharmProjects\Meta_description_1.xlsx"

row = DDT_for_HCM.getRowCount(path, "Sheet1")
column = DDT_for_HCM.getColumnCount(path, "Sheet1")

for r in range(2,row+1):
    website = DDT_for_HCM.readData(path,"Sheet1",r,1)

    driver.get(website)
    driver.maximize_window()

    driver.find_element(By.ID,"i0116").send_keys("shantanu.khanna@hexagon.com")
    driver.find_element(By.ID,"idSIButton9").click()
    driver.find_element(By.ID,"i0118").send_keys("$Welcome2Hexagon$")
    driver.find_element(By.XPATH,"/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input").click()
    driver.find_element(By.ID,"idChkBx_SAOTCAS_TD").click()
    driver.find_element(By.ID,"KmsiCheckboxField").click()
    driver.find_element(By.ID,"idSIButton9").click()

    var = driver.find_element(By.XPATH, "//meta[@name='description']")
    if var:
        DDT_for_HCM.writeData(path, "Sheet1", r, 2, print(var.get_attribute("content")))

driver.close()
driver.quit()