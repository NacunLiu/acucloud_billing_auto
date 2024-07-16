import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# drop-menu/scroll/pop-window//login-fail/snap-shot/
# 创建WebDriver实例
driver = webdriver.Chrome('./chromedriver-win64/chromedriver.exe')

# 打开页面
driver.get(
    'http://localhost:63342/pythonAcuCloudApiAutoFrameWork/script_9.html?_ijt=5t0v2re0f08ejpm4t1dtofgnou&_ij_reload=RELOAD_ON_SAVE')
# 使用本地文件路径

# 查找下拉菜单
dropdown = Select(driver.find_element(By.CLASS_NAME, 'meter-test'))

# 匿名选择
dropdown.select_by_value('810')  # 通过value属性值选择
# 或者
# dropdown.select_by_index(0)  # 通过索引选择

# 实名选择
# dropdown.select_by_visible_text('Volvo')  # 通过可见文本选择

# 获取当前选中的选项
selected_option = dropdown.first_selected_option
print(selected_option.text)  # 输出 "Volvo"

# 关闭浏览器
driver.quit()
