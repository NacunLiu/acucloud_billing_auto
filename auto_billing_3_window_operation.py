import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver with ChromeDriverManager会自动下载对应的driver，不需要再手动配置
# service = ChromeService(executable_path=ChromeDriverManager().install())
service = ChromeService()
options = webdriver.ChromeOptions()

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome('./chromedriver-win64/chromedriver.exe')
driver.get('https://dev.acucloud.accuenergy.com')
driver.implicitly_wait(10)
time.sleep(3)
# 窗口最大化
driver.maximize_window()
time.sleep(3)
# 设置窗口大小
driver.set_window_size("960", "540")
time.sleep(3)
# 设置窗口位置
driver.set_window_position("200", "100")
time.sleep(3)

driver.maximize_window()
time.sleep(10)

user = driver.find_element(By.XPATH, "//input[@type='text']")
pwd = driver.find_element(By.XPATH, "//input[@type='password']")
cbx = driver.find_element(By.XPATH, "//input[@type='checkbox']")
smt = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
time.sleep(3)

user.send_keys('nacun.liu@accuenergy.com')
# pwd.send_keys('12345676')
# time.sleep(1)
# pwd.clear()

time.sleep(3)

user.clear()
pwd.clear()

time.sleep(3)

user.send_keys("nacun.liu@accuenergy.com")
pwd.send_keys("Toz13547")
# cbx.click()
# time.sleep(3)

# 登录停留10秒进行观察
smt.click()
time.sleep(10)

# 捕获弹窗
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Close']")))
alert.click()

# 获取help链接元素，进行登录
help_link = driver.find_element(By.CSS_SELECTOR, ".navbar-right li:nth-child(3) a")
help_link.click()
time.sleep(10)
# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(3)


# 浏览器后退
driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

# refresh刷新当前页面
driver.refresh()
time.sleep(3)

# title获取前端页面title, 用它判断是否已经打开当前页面，也可以用title来切换窗口
title = driver.title
print(title)
time.sleep(3)

# current_url 获取当前页面的url
url = driver.current_url
print(url)
time.sleep(3)

# driver.quit()关闭浏览器所有窗口
driver.close()
time.sleep(3)
# 关闭当前窗口
driver.quit()

# # Conf ID# 378875201714
# # clerkspublic@markham.ca
# # 905 - 477 - 7000 ext 2366
