import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# 本章内容:下拉框,警告弹窗,frame标签的处理

# 通过driver里封装的switch_to方法可以进行各种切换操作：切换到警告框 driver.switch_to.alert 切换到frame driver.switch_to.frame(id/name)
# 从frame返回到主页面 driver.switch_to.default_content()
# 切换到新的窗口 driver.switch_to.window(handle)

# 下拉选择框可以通过CSS直接处理，也可以通过selenium中封装的Select类去处理，而且会显得更方便
# 使用Select类，先创建一个对象,并且传入select元素，select = Select(element)
# 之后操作select进行选择,操作方法有select_by_index(index) select_by_value(value) select_by_visible_text(text)

# 警告弹窗有三种 alert, confirm, prompt
# 通过driver.switch_to.alert 切换到弹窗
# 处理弹窗可以使用三种方法：取消 alert.dismiss() 确认 alert.accept() 获取文本 alert.text

# 滚动条的处理,页面的加载是随着滚动条的向下滚动而逐渐加载或者有些场景只有滚动条滚动到底之后才能进行一些操作
# selenium没有提供直接操作滚动条的API,但是它提供了可执行JavaScript脚本的方法, 因此我们可以通过操作JS脚本来操作滚动条
# js = 'window.scrollTo(0,1000)' driver.execute_script(js) 总共分为两步:第一步包裹js语句 第二步使用driver去执行js语句

# frame表单切换
# 第一步driver.switch_to.frame(frame_reference) 切换到指定的frame,frame_reference可以为三个值：frame的name,id或者直接定位frame元素
# 第二步恢复页面 driver.switch_to.default_content()


# drop-menu/scroll/pop-window//login-fail/snap-shot/
# 创建WebDriver实例
service = Service('./chromedriver-win64/chromedriver.exe')
options = Options()
driver = selenium.webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
driver.maximize_window()
# 打开页面
driver.get(
    'http://127.0.0.1:5500/script_9.html')
actions = ActionChains(driver)


# 查找下拉菜单
dropdown = Select(driver.find_element(By.CLASS_NAME, 'meter-test'))
time.sleep(3)
print(dropdown._el.get_attribute('class'))
print(dropdown._el.tag_name)

# 匿名选择
dropdown.select_by_value('810')  # 通过value属性值选择
time.sleep(3)
# 或者
# dropdown.select_by_index(0)  # 通过索引选择

# 实名选择
# dropdown.select_by_visible_text('Volvo')  # 通过可见文本选择

# 获取当前选中的选项
selected_option = dropdown.first_selected_option
print(selected_option.text)  
time.sleep(3)

# 查找并且点击警告弹窗
# 使用Actions类中封装的鼠标方法,点击元素
actions.click(driver.find_element(By.CSS_SELECTOR, 'input[value="alert"]')).perform()
time.sleep(3)
alert = driver.switch_to.alert
time.sleep(3)
alert.dismiss()

#查找并且点击确认弹窗
actions.click(driver.find_element(By.CSS_SELECTOR, 'input[value="confirm"]')).perform()
time.sleep(3)
confirm = driver.switch_to.alert
time.sleep(3)
confirm.accept()

# 查找并点击提示弹窗,并且获取弹窗中的文字内容
actions.click(driver.find_element(By.CSS_SELECTOR, 'input[value="prompt"]')).perform()
time.sleep(3)
pt = driver.switch_to.alert
time.sleep(3)
print(pt.text)
pt.accept()

# 向下滑动滚动条查找按钮
js = 'window.scrollTo(0, 2000)'
driver.execute_script(js)
time.sleep(3)
actions.click_and_hold(driver.find_element(By.CSS_SELECTOR, '.hidden-button')).perform()
time.sleep(3)
# 松开鼠标按键
actions.release().perform()

# 将driver切换到frame
driver.switch_to.frame("reg")
driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys("nacun.liu@accuenergy.com")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(Keys.CONTROL, 'a')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(Keys.CONTROL, 'x')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(Keys.CONTROL, 'v')
# 将driver切换回到原来的页面
driver.switch_to.default_content()


actions.click_and_hold(driver.find_element(By.CSS_SELECTOR, '.hidden-button')).perform()
time.sleep(3)
actions.release().perform()
time.sleep(1)

# 关闭浏览器
driver.quit()
