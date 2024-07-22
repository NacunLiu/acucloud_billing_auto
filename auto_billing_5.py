import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# 使用元素的get_attributes方法来获取元素的对应属性
driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')
driver.get('http://192.168.60.105:3000')
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