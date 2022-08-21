import DDT_Rate_Calculator

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser = Service(executable_path="C:\\Users\Shantanuk\PycharmProjects\pythonProject-demo1\driver\chromedriver.exe")
driver = webdriver.Chrome(service= ser)

driver.get("https://app.shipway.com/merchant.php?dispatch=auth.login_form&return_url=merchant.php")
driver.maximize_window()

path ="C:\\Users\Shantanuk\PycharmProjects\Login_1.xlsx"

row = DDT_Rate_Calculator.getRowCount(path,"Sheet1")
column = DDT_Rate_Calculator.getColumnCount(path,"Sheet1")

for r in range(2,row+1):
    username = DDT_Rate_Calculator.readData(path,"Sheet1",r,1)
    password = DDT_Rate_Calculator.readData(path,"Sheet1",r,2)

    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.NAME,"dispatch[auth.login]").click()

    if driver.title == "Orders :: View orders - Administration panel":
        print("Test passed")
        DDT_Rate_Calculator.writeData(path,"Sheet1",r,3,"test passed")
        driver.find_element(By.XPATH,
            "//body/div[@id='main_column']/div[1]/div[1]/div[1]/div[1]/div[1]/ul[2]/li[2]/a[1]").click()
        driver.find_element(By.XPATH,"//a[contains(text(),'Sign out')]").click()
    else:
        print("test failed")
        DDT_Rate_Calculator.writeData(path,"Sheet1",r,3,"test failed")
        driver.refresh()

driver.close()
driver.quit()