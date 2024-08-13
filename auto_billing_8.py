import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 本章内容:隐式等待和显示等待
# 隐式等待只需要设置一次对所有元素有效
# 显示等待只对单个元素有效 在selenium中，把显示等待的相关内容封装在WebDriverWait中

try:
    chrome_service = Service('./chromedriver-win64/chromedriver.exe')
    chrome_options = Options()
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
except Exception as e:
    driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')

driver.get('https://dev.acucloud.accuenergy.com')
driver.maximize_window()

driver.implicitly_wait(10)
time.sleep(3)

wait = WebDriverWait(driver, 3, 0.1)
user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

user.send_keys('nacun.liu@accuenergy.com')
pwd.send_keys('Toz13547')
login.click()
time.sleep(10)

driver.implicitly_wait(3)

actions = ActionChains(driver)
actions.context_click()
time.sleep(10)

driver.quit()
