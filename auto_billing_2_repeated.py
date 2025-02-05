import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 此模块为重复内容，可以不看
driver = webdriver.Edge('./edgedriver_win64/msedgedriver.exe')
driver.get('http://127.0.0.1:5500/practice2.html')
time.sleep(8)
# ac810 = driver.find_element(By.CSS_SELECTOR, ".test tbody tr:first-child td:nth-child(1)")
ac810 = driver.find_element(By.XPATH, "//tr/td")
print(ac810.text)
user = driver.find_element(By.XPATH, "//input[@type='text']")
pwd = driver.find_element(By.XPATH, "//input[@type='password']")
cbx = driver.find_element(By.XPATH, "//input[@type='checkbox']")
smt = driver.find_element(By.XPATH, "//input[@type='submit']")

user.send_keys('nacun')
pwd.send_keys('123')
cbx.click()
smt.click()
# driver.quit()