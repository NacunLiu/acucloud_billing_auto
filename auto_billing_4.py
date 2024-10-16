import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# get element attributes
# size text get_attribute() is_displayed is_enabled is_selected
driver = selenium.webdriver.Edge('./edgedriver_win64/msedgedriver.exe')
driver.get('http://127.0.0.1:5500/practice2.html')
time.sleep(10)

user = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
print(user.size)
att = user.get_attribute("value")
print(att)
print(user.is_displayed())

cbx = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
cbx.click()
time.sleep(3)
print(f"the checkbox is selected? {cbx.is_selected()}")


# get table data
driver = selenium.webdriver.Edge('./edgedriver_win64/msedgedriver.exe')
driver.get('http://localhost:3000/')
#
# # 获取列表
# table = driver.find_element(By.CSS_SELECTOR, 'table')
#
# # 获取表头
headers = table.find_elements(By.XPATH, ".//thead//th")
header_names = [header.text for header in headers]
#
print(header_names)

# # 获取表格体中的数据，形成一个二维数组
rows = table.find_elements(By.XPATH, ".//tbody//tr")
table_data = []
#
for row in rows:
    cells = row.find_elements(By.XPATH, ".//td")
    row_data = [cell.text for cell in cells]
    table_data.append(row_data)
#
# # 打印表格
print(header_names)
for abc in table_data:
    print(abc)


# 使用selenium 操作鼠标键盘
driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')
driver.get('https://dev.acucloud.accuenergy.com')

time.sleep(3)

inputs = driver.find_elements(By.TAG_NAME, 'input')
btns = driver.find_elements(By.TAG_NAME, 'button')

# 元素渲染需要时间，如果无法直接定位到元素，就需要等带接秒的时间
inputs[0].send_keys('nacun.liu@accuenergy.com')
inputs[1].send_keys('Toz13547')
time.sleep(3)

btns[1].click()

context_click(element)右击  double_click(element)双击 drag_and_drop(source, target)模拟鼠标拖动
move_to_element(element)悬停 perform()执行以上操作，之前只是添加到ActionChains类里边，并没有执行，需要实例.perform()执行

