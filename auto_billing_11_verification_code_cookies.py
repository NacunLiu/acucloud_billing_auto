import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 本章内容：对测试结果进行截图 验证码的处理
# 使用 driver.get_screenshot_as_file('img_path'), ()内填入保存图片的地址


# 验证码的处理办法：去掉验证码(测试环境下) 设置万能验证码(测试和生产环境) 验证码识别技术(通过python-tesseract来识别图片验证码) 记录cookie(通过记录cookie进行跳过登录)
# 使用cookie绕过验证码的方法：1.通过手动登录成功之后，服务器会返回一个有效的带有sessionid的cookie
# 2.通过driver.get_cookies获取cookie
# 3.在后续的请求中将获取到的cookie添加到请求头header中携带认证的cookie进行请求操作就可以有效的绕开验证码
# 当用户登录成功后服务器会在服务端创建一个sessionid，并且储存在cookie中，这个sessionid会随着cookie在后续的请求中被发送给服务器，服务器会恢复相关会话信息
# session是一种临时的会话，保存丰富的客户信息，但是存储在服务器端所以更安全，而且只要携带seesionid，那么在后续访问都可以恢复正常会话
# cookie是由服务器产生但是存储在客户端浏览器中的轻量数据不安全，不宜存放敏感信息
# 获取单个cookie driver.get_cookie(name) 获取所有cookie driver.get_cookies() 添加cookie driver.add_cookie(cookie_dict)


try:
    chrome_service = Service('./chromedriver-win64/chromedriver.exe')
    chrome_options = Options()
    driver = selenium.webdriver.Chrome(service=chrome_service, options=chrome_options)
except Exception as e:
    driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')

driver.get('https://dev.acucloud.accuenergy.com')
actions = ActionChains(driver)

driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(3)

usr = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys('nacun.liu@accuenergy.com')
pwd = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('Toz13547')
time.sleep(3)
login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
time.sleep(3)

# at = driver.switch_to.alert
# at.dismiss()
btn = driver.find_element(By.CLASS_NAME, 'ant-btn')
btn.click()

analysis = driver.find_element(By.CSS_SELECTOR, '.ant-menu-vertical li:nth-child(4)')
analysis.click()
time.sleep(3)

# 对显示结果进行截图并保存,使用时间戳可以保存多张图片
driver.get_screenshot_as_file(f'./test/{time.strftime("%Y-%m-%d %H_%M_%S")}.png')
time.sleep(3)

cookies = driver.get_cookies()
print(cookies)
time.sleep(3)

# 添加一个cookie
driver.add_cookie({'name': '_user', 'value': 'nacun'})
time.sleep(3)

# 再次点击发送请求之后获取cookie
actions.click(driver.find_element(By.LINK_TEXT, "Home")).perform()
print(f'new cookies are: {driver.get_cookies()}')
# 打开开发者工具，查看request cookie，会发现新添加的cookie内容
time.sleep(30)
driver.refresh()
time.sleep(10)

driver.quit()
