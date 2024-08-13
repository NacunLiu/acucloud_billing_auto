import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from seleniu.webdriver.support import Expected_Conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# 使用元素的get_attributes方法来获取元素的对应属性
try:
    service = Service('./chromedriver-win64/chromedriver.exe')
    options = Options()
    driver = selenium.webdriver.Chrome(service=service, options=options)
except Exceptions as e:
    driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')

driver.get('http://192.168.60.105:3000')
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10, 0.1)
time.sleep(3)

# 获取页面第一个输入框的大小
size = driver.find_element(By.TAG_NAME, "input")
# 获取页面第一个超文本连接中的内容
content = driver.find_element(By.TAG_NAME, "a").get_attribute("href")
span = driver.find_element(By.TAG_NAME, "span")

print(f'the size of the first input is: {size}')
print(content)
print(f"span is available to see: {span.is_displayed()}")

time.sleep(3)
driver.quit()