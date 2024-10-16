import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = selenium.webdriver.Chrome('chromedriver-win64/chromedriver.exe')
driver.get("https://acucloud.accuenergy.com")
time.sleep(10)

input = driver.find_element(By.XPATH, "//input[@type='text']")
input.send_keys("abcde")
time.sleep(3)
content = input.get_attribute("value")
content.Key_
print(content)