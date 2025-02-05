import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get window handle has three functions: driver.current_window_handle, driver.window_handles, driver.switch_to.window(handle)
chrome_service = Service('chromedriver-win64\chromedriver.exe')
chrome_options = Options()
#  this method is not supported after selenium 4.x driver = webdriver.Chrome('chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get('http://127.0.0.1:5500/script_14.html')
sleep(10)
driver.implicitly_wait(10)
# get current window handle
current_handle = driver.current_window_handle
screenshot_path = "./test/sc1.png"
driver.save_screenshot(screenshot_path)
print(f'current window handle is : {current_handle}')
print(f'current window title is {driver.title}')

wait = WebDriverWait(driver, 10, 1)
dev = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "dev")))
# sleep(20)

dev.click()
sleep(20)

handles = driver.window_handles
# as window handles in the list reflects the open time order, the later opened, the index is bigger
# if just wanna to switch to the latest window handle can use
# driver.switch_to.window(handles[-1])
# when there are only 2 window handles we can use the following method:
for handle in handles:
    sleep(3)
    if handle != current_handle:
        driver.switch_to.window(handle)
        print(driver.title)
        break
# If there are more than two window handles, we can use driver.title == 'expected' to find the correct window handle
# for handle in handles:
#     driver.switch_to(handle)
#     print(driver.title)
#     break

sleep(3)

driver.close()
