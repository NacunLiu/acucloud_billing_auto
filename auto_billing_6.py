import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# 使用ActionChains类来操作鼠标的接口进行单击，双击，拖拽等操作，selenium将所有鼠标操作封装在ActionChains类中
# 在需要导入的类名的最后一个字母后边使用"Ctrl+Alt+Space"或者"Alt+Enter"的快捷键进行自动导包
# 相关操作有，右击actions.context_click(element),单击actions.click(element),双击actions.double_click(element)
# 拖拽actions.drag_and_drop(source, target), 悬停actions.move_to_element(element)
# perform()，以上所有的方法必须通过.perform()才会执行，否则只是将相应方法添加到了类中

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
# 点击这个按钮, 任何鼠标操作后边都需要加上.perform()才能开始执行操作
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


