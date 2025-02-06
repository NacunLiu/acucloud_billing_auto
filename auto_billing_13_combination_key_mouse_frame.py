import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from time import sleep

chrome_service = Service('chromedriver-win64/chromedriver.exe')
chrome_options = Options()
driver = selenium.webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get('http://127.0.0.1:5500/script_13.html')
# iframe related operation the original element is not on the page so we need to switch to iframe first
driver.implicitly_wait(10)
action = ActionChains(driver)
wait = WebDriverWait(driver, 10, 0.5)
sleep(3)
driver.switch_to.frame("acucloud")
usr = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
pwd = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
sbt = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")

time.sleep(1)
usr.send_keys("admin")

time.sleep(1)
pwd.send_keys("admin123")

time.sleep(1)
usr.send_keys(Keys.CONTROL, "A")
sleep(1)

usr.send_keys(Keys.CONTROL, "C")
time.sleep(1)

usr.send_keys(Keys.DELETE)
sleep(2)

usr.send_keys(Keys.CONTROL, "V")
time.sleep(1)

sbt.click()
time.sleep(1)

driver.switch_to.default_content()

s2 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s2")))
s3 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s3")))

action.click()
for i in range(10):
    if i % 2 == 0:
        action.move_to_element(s2).perform()
    else:
        action.move_to_element(s3).perform()
    time.sleep(0.5)

time.sleep(1)

driver.close()