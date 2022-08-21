import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def is_element_present(how, what):
    try:
        driver.find_element(by=how,value=what)
        return True
    except NoSuchElementException:
        return False

ser = Service(executable_path="driver\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.implicitly_wait(20)

driver.get("https://app.shipway.com/merchant.php?dispatch=auth.login_form&return_url=merchant.php")
driver.find_element(By.ID,"username").send_keys("Shantanu.khanna1@shipway.in")
driver.find_element(By.ID,"password").send_keys("Shaan@123")
driver.find_element(By.NAME,"dispatch[auth.login]").click()
time.sleep(2)
driver.refresh()
dropdown = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div/div[2]/ul/li[7]/a")
action = ActionChains(driver)
action.move_to_element(dropdown).perform()
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div/div[2]/ul/li[7]/ul/li[2]").click()
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/ul/li[2]/a").click()
driver.find_element(By.ID,"pickup_pincode").send_keys("110059")
driver.find_element(By.ID,"drop_pincode").send_keys("120001")
driver.find_element(By.NAME,"dispatch[aggregation_rate_card.calculate_price]").click()

if driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div[2]/"
                               "div/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[7]/span").text =="47.20":
    time.sleep(4)
    print("passed")
else:
    print("test failed")
driver.close()
driver.quit()