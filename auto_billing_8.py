import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service('./chromedriver-win64/chromedriver.exe')
options = Options()
driver = selenium.webdriver.Chrome(service=service, options=options)
driver.get('https://dev.acucloud.accuenergy.com')
driver.maximize_window()

driver.implicitly_wait(10)
time.sleep(3)

wait = WebDriverWait(driver, 3)
user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

user.send_keys('nacun.liu@accuenergy.com')
pwd.send_keys('Toz13547')
login.click()
time.sleep(10)

driver.implicitly_wait(3)
driver.quit()

