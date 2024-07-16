import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')
driver.get('https://dev.acucloud.accuenergy.com')

driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)

usr = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys('nacun.liu@accuenergy.com')
pwd = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('Toz13547')
time.sleep(3)
login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(3)

# at = driver.switch_to.alert
# at.dismiss()
btn = driver.find_element(By.CLASS_NAME, 'ant-btn')
btn.click()

analysis = driver.find_element(By.CSS_SELECTOR, '.ant-menu-vertical li:nth-child(4)')
analysis.click()
time.sleep(2)

driver.quit()
