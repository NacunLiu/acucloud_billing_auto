from selenium.webdriver.common.by import By


# __init__是包与文件夹最主要的区别，__init__中的元素可以直接通过包名.的形式在其他模块中使用，比如在其他模块中使用page.login_username
# 登录页面元素配置信息
login_link = By.PARTIAL_LINK_TEXT, "Sign in"
login_username = By.CSS_SELECTOR, "input[type='text']"
login_password = By.CSS_SELECTOR, "input[type='password']"
submit = By.CSS_SELECTOR, "button[type='submit']"
login_error = By.CSS_SELECTOR, ".si-failure"

# location for installation navi
installation_navi = By.XPATH, "//ul/li/span[text()='Installation']"
device_navi = By.XPATH, "//div/a[text()='Device']"

