import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = selenium.webdriver.Chrome(executable_path="./chromedriver-win64/chromedriver.exe")
driver.get('http://192.168.60.105:3000')
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
# 定位Start按钮
ipt1 = driver.find_element(By.CSS_SELECTOR, "input[value='Start']")
print(ipt1)
# 点击这个按钮
actions.click(ipt1).perform()
time.sleep(3)
# 双击这个按钮
actions.double_click(ipt1).perform()
time.sleep(3)
# 按住这个按钮
actions.click_and_hold(ipt1).perform()
# 拖拽这个按钮
actions.drag_and_drop_by_offset(ipt1, 200, 400)
actions.click(ipt1)


