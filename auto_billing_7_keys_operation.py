import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# 本章内容:对键盘的操作
# 基本操作 key_up key_down send_keys()
# 使用actions.key_down(Keys.CONTROL)来模拟键盘操作按下按键，只能传递一个参数，后边必须跟随actions.key_up(Keys.CONTROL)来释放按键
# 如果不跟随key_up释放按键会一直保持键盘按下状态
# 虽然actions.key_down()只接受一个参数,不可以在里边同时传递多个键盘值，但是可以在语句中调用链中组合操作
# send_keys()可以接受多个参数，但是它不会hold，而且不会同时执行，对每一个键盘值按顺序一个一个执行，每个只是敲击一下，所以send_keys('abc')和
# send_keys('a').send_keys('b').send_keys('c')是一样的效果，想要执行多个按键一起按需要使用key_down()
# 比如: actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()来执行全选操作
# 键盘的操作被封装在了Keys类中，使用keys.'键名'进行操作
# send_keys('aculink810')输入指定文本内容
# send_keys(Keys.ENTER/TAB/ESCAPE/BACK_SPACE/DELETE/SAPCE/SHIFT/CONTROL)特殊键盘操作
# send_keys用于发送文本，操作按键和上传三个方面
# 组合按键和复杂操作actions.key_down(Keys.CONTROL).send_keys('a').key_up(CONTROL).perform()
# 显示等待和隐式等待 隐式等待：driver.implicitly_wait(10)，找到元素直接执行，未找到会每隔0.5秒尝试一次知道设置的timeout时间
# 显示等待： webDriverWait(driver, timeout=10, poll_frequency=0.5)默认等待时间是0.5秒找一次
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
# 鼠标悬在类名上，按住CONTROL点击类名进入底层查看内容
try:
    chrome_service = Service('./chromedriver-win64/chromedriver.exe')
    chrome_options = Options()
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
except Exception as e:
    driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')

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


