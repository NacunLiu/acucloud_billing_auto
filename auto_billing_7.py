import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


# 键盘的操作被封装在了Keys类中，使用keys.'键名'进行操作
# send_keys('aculink810')输入指定文本内容
# send_keys(keys.ENTER/TAB/ESCAPE/BACK_SPACE/DELETE/SAPCE/SHIFT/CONTROL)特殊键盘操作
# 组合按键和复杂操作actions.key_down(Keys.CONTROL).send_keys('a').key_up(CONTROL).perform()
# 显示等待和隐式等待 隐式等待：driver.implicitly_wait(10)，找到元素直接执行，未找到会每隔0.5秒尝试一次知道设置的timeout时间
# 显示等待： webDriverWait(driver, timeout=10, poll_frequency=0.5)默认等待时间是0.5秒找一次
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
service = Service('./chromedriver-win64/chromedriver.exe')
options = Options()
driver = selenium.webdriver.Chrome(service=service, options=options)
driver.get('https://dev.acucloud.accuenergy.com/')
driver.maximize_window()
actions = ActionChains(driver)

driver.implicitly_wait(10)

user = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
pwd = driver.find_element(By.XPATH, '//input[@type="password"]')

user.send_keys("nacun1")
time.sleep(3)

user.send_keys(Keys.CONTROL, "a")
time.sleep(3)

user.send_keys(Keys.CONTROL, "x")
time.sleep(3)

pwd.send_keys(Keys.CONTROL, "v")
time.sleep(3)
driver.quit()


