import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# 使用ActionChains类来操作鼠标的接口进行单击，双击，拖拽等操作，selenium将所有鼠标操作封装在ActionChains类中
# 在需要导入的类名的最后一个字母后边使用"Ctrl+Alt+Space"或者"Alt+Enter"的快捷键进行自动导包
# 相关操作有，右击actions.context_click(element),单击actions.click(element),双击actions.double_click(element)
# 拖拽actions.drag_and_drop(source, target)只在App自动化里使用, 悬停actions.move_to_element(element)
# perform()，以上所有的方法必须通过.perform()才会执行，否则只是将相应方法添加到了类中

service = Service('./chromedriver-win64/chromedriver.exe')
options = Options()
driver = selenium.webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
driver.get('http://127.0.0.1:5500/script_6_mouse_key.html?#')
time.sleep(3)

# 设置浏览器窗口大小
driver.set_window_size(1260,1080)
time.sleep(3)

# 浏览器窗口定位
driver.set_window_position(100,100)
time.sleep(3)

# 浏览器窗口最大化
driver.maximize_window()

# 创建鼠标移动对象,传递driver使得selenium知道在哪个浏览器的上下文中进行操作
actions = ActionChains(driver)
time.sleep(3)
# 定位sumbit按钮
submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
# print(ipt1)
# 点击这个按钮, 任何鼠标操作后边都需要加上.perform()才能开始执行操作
actions.click_and_hold(submit).perform()
time.sleep(3)

# 定位username双击选中
username = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
actions.double_click(username).perform()
time.sleep(3)
actions.double_click(username).perform()
time.sleep(3)
# 拖拽这个按钮
actions.drag_and_drop_by_offset(submit, 200, 400).perform()
time.sleep(3)


