import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# get element attributes获取HTML元素的标签内属性值 不包括标签内文本或者CSS属性
# 注意element.get_attribute("value")是用来获取诸如 id class type value checked href src等的写在标签里的附加信息

# 比如 <input type="text" id="user" name="username" value="admin" disabled> 

# | Attribute  | 含义                     |
# | ---------- | ---------------------- |
# | `type`     | 控件类型（如 text, password） |
# | `id`       | 元素唯一标识                 |
# | `name`     | 表单字段名                  |
# | `value`    | 当前输入值                  |
# | `disabled` | 是否被禁用（无值时返回 `"true"`）  |

# el = driver.find_element(By.CSS_SELECTOR, "#user")
# el.get_attribute("type"), el.get_attribute("id"), el.get_attribute("name"), el.get_attribute("value")
# 但是不能获取CSS样式属性 比如 text 或者 color之类的样式值

# <a> hello </a> 这个'hello'是标签内文本 不能使用get_attribute()获取
# 直接使用 el.text 获取

# 如果要获取CSS样式 那么使用 el.value_of_css_property()获取CSS 属性例如 width, height, padding, margin, display, visibility, opacity等
# 比如 el.value_of_css_property("color"), el.value_of_css_property("font-size"), el.value_of_css_property("background-color")

# 使用el.is_selected(), el.is_enabled(), el.is_displayed()来获取元素是否被选中或者开启或者显示在页面上(隐藏时返回False)


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
table = driver.find_element(By.CSS_SELECTOR, 'table')
#
# # 获取表头
headers = table.find_elements(By.XPATH, ".//thead//th")
header_names = [header.text for header in headers]
#
print(header_names)

# # 获取表格体中的数据，形成一个二维数组
rows = table.find_elements(By.XPATH, ".//tbody//tr") # 这个XPATH语句表示在当前元素中查找的所有tbody子元素的所有tr子元素
#  . 表示当前元素, //表示所有直接和非直接子元素, 在元素后面加上[@attribute_name=value]查找具有特定属性值的元素
#  find_elements(By.XPATH, ".//tbody//*[@class='power']") 查找当前元素的所有tbody子元素的所有子元素中类名为power的元素, *表示所有元素
# find_elements(By.XPATH, ".//tbody//tr[@class='power']") 查找当前元素的所有tbody子元素的所有类名为power的tr子元素

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

# context_click(element)右击  double_click(element)双击 drag_and_drop(source, target)模拟鼠标拖动
# move_to_element(element)悬停 perform()执行以上操作，之前只是添加到ActionChains类里边，并没有执行，需要实例.perform()执行


