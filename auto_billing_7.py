import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


driver = selenium.webdriver.Chrome("./chromedriver-win64/chromedriver.exe")
driver.get('https://dev.acucloud.accuenergy.com')
driver.maximize_window()
actions = ActionChains(driver)

driver.implicitly_wait(10)
# send_keys('aculink810')输入指定文本内容
# send_keys(keys.ENTER/TAB/ESCAPE/BACK_SPACE/DELETE/SAPCE/SHIFT/CONTROL)特殊键盘操作
# 组合按键和复杂操作actions.key_down(Keys.CONTROL).send_keys('a').key_up(CONTROL).perform()
user = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
pwd = driver.find_element(By.XPATH, '//input[@type="password"]')

user.send_keys("nacun1")
user.send_keys(Keys.CONTROL, "a")
user.send_keys(Keys.CONTROL, "c")
time.sleep(2)
pwd.send_keys(Keys.CONTROL, "v")


time.sleep(2)
driver.quit()
# 显示等待和隐式等待 隐式等待：driver.implicitly_wait(10)
# 显示等待： webDriverWait(driver, timeout=10, poll_frequency=0.5)默认等待时间是0.5秒找一次

