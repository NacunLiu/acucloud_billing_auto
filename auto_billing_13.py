import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = selenium.webdriver.Chrome('chromedriver-win64/chromedriver.exe')
driver.get('http://127.0.0.1:5500/script_13.html')
# iframe related operation the original element is not on the page so we need to switch to iframe first
driver.implicitly_wait(10)
sleep(3)
driver.switch_to.frame("acucloud")
usr = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
pwd = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
sbt = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

usr.send_keys("admin")
pwd.send_keys("admin123")

usr.send_keys(Keys.CONTROL, "A")
sleep(3)
usr.send_keys(Keys.CONTROL, "C")
usr.send_keys(Keys.DELETE)
sleep(2)
usr.send_keys(Keys.CONTROL, "V")
sbt.click()

driver.switch_to.default_content()
driver.close()