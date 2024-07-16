import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 8 different ways to locate an element: By.ID By.CLASS_NAME
# By.TAG_NAME By.LINK_TEXT By.PARTIAL_LINK_TEXT 
# By.LINK_TEXT 用于查找与提供的完整链接文本匹配的 <a> 元素
# By.PARTIAL_LINK_TEXT 用于查找包含提供的部分链接文本的 <a> 元素
# By.XPATH By.CSS_SELECTOR: for XPATH use //div[@id="main"] format  //+tagname[@attribute="value"] //a[text()="content"]文本内容或者使用包含某个内容 //a[contains(text(), "content")]


# 标准操作窗口最大化，设置隐式等待时间
chrome_service = Service('./chromedriver-win64/chromedriver.exe')
chrome_options = Options()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get('https://dev.acucloud.accuenergy.com')
driver.maximize_window()

# 设置隐式等待和显示等待
driver.implicitly_wait(10);
wait = WebDriverWait(driver, 10)

#使用XPATH定位输入框和密码框
user = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
pass_word = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))

# 使用CSS_SELECTOR定位checkbox和提交按钮
check_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']")))
submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

# 填入响应的数据
user.send_keys("nacun.liu@accuenergy.com")
pass_word.send_keys("Toz13547")
time.sleep(3)

# check和uncheck 记忆框
check_box.click()
time.sleep(3)
check_box.click()

# 点击登录
submit.click()
time.sleep(10)

# 关闭浏览器
driver.quit()