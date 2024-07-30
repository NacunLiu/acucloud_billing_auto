
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 本章内容:多窗口的切换
# 在常用的网页弹出框有三种alert confirm prompt
# 使用driver.current_window_handle获取当前窗口句柄 使用dirver.window_handles获取所有窗口句柄
# 第一步:获取当前窗口句柄 第二步:点击超链接页面 第三步:获取所有窗口句柄 第四步:判断不是当前窗口句柄则切换


service =  Service('./chromedriver-win64/chromedriver.exe')
options = Options()
driver = selenium.webdriver.Chrome(service=service, options=options)
driver.get('http://127.0.0.1:5500/script_10.html')
driver.maximize_window()
driver.implicitly_wait(3)
time.sleep(3)
try:
    # 获取对话弹框
    alert = driver.switch_to.alert
    # alert.text   alert.accept()   alert.dismiss()
    print(alert.text)
    time.sleep(3)
    alert.dismiss()
except Exception as e:
    print(f'error occurred as e')
time.sleep(1)
js = "window.scrollTo(0, 2000)"
driver.execute_script(js)
time.sleep(1)

actions = ActionChains(driver)

# 获取当前窗口句柄
current_window = driver.current_window_handle
print("当前窗口句柄为", current_window)
actions.click(driver.find_element(By.TAG_NAME, 'a')).perform()
time.sleep(3)

# 获取所有窗口的句柄
window_list = driver.window_handles
print(window_list)
time.sleep(3)

for handle in window_list:
    if handle != current_window:
       driver.switch_to.window(handle)

usr = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
usr.send_keys('nacun.liu@accuenergy.com')
time.sleep(3)
driver.quit()
