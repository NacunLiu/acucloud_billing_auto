import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# 本章内容:隐式等待和显示等待
# 隐式等待 driver.implicitly_wait(10) only takes 1 argument is the timeout, it does not take other argument like poll frequency, default 0.5 is immutable
# it will wait 10 seconds until element showup or it will raise NoSuchElementException after timeout, if element is found it will immediately move on
# 只需要设置一次对所有元素有效
# 显示等待只对单个元素有效 在selenium中，把显示等待的相关内容封装在WebDriverWait中, 使用wait = WebDriverWait(driver)创建一个等待对象，之后wait.until()会按 poll frequency去不停的调用里边的方法，
# until()接受一个可以调用的函数，并且函数的返回值如果是找到的元素就会直接返回，如果是0就会继续等待，而且能捕获异常，如果返回的是NoSuchElement异常，那么它会过滤异常，继续等待下一次调用
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))和 wait.until(driver.find_element(By.CSS_SELECTOR, 'input[type="text"]'))的区别
# presence_of_element_located的底层也是在调用find_element()方法，但是find_element()是一条语句，而不不是一个函数，根本问题在于执行顺序，语句会先于until执行，函数会后于until执行
# 如果直接写，那么python解释器在读到这一行的时候会先执行until里边的这条语句，之后如果找不到元素就会直接报异常，程序崩溃，until还没有执行，无法捕获异常
# 如果是一个函数EC那么，会先执行until,然后将控制权交给里边的函数，继续执行里边的EC，将返回结果无论是什么先给until，控制权交给until继续执行，并不会在EC报异常的时候直接终止程序


try:
    chrome_service = Service('./chromedriver-win64/chromedriver.exe')
    chrome_options = Options()
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
except Exception as e:
    driver = selenium.webdriver.Chrome('./chromedriver-win64/chromedriver.exe')

driver.get('https://dev.acucloud.accuenergy.com')
driver.maximize_window()

driver.implicitly_wait(10)
time.sleep(3)

wait = WebDriverWait(driver, 3, 0.1)
user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

user.send_keys('nacun.liu@accuenergy.com')
pwd.send_keys('Toz13547')
login.click()
time.sleep(10)

driver.implicitly_wait(3)

actions = ActionChains(driver)
actions.context_click()
time.sleep(10)

driver.quit()
