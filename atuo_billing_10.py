# 在常用的网页弹出框有三种alert confirm prompt
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')
driver.get('http://127.0.0.1:5500/script_10.html')
driver.maximize_window()
driver.implicitly_wait(3)
time.sleep(10)
try:
    # 获取对话弹框
    alert = driver.switch_to.alert
    # alert.text   alert.accept()   alert.dismiss()
    print(alert.text)
    time.sleep(3)
    alert.dismiss()
except Exception as e:
    print(f'error occurred as e')
time.sleep(3)
js = "window.scrollTo(0, 2000)"
driver.execute_script(js)
time.sleep(10)

driver.quit()
